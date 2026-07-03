import streamlit as st
from src.data_loader import load_csv
from src.profiler import generate_profile
from src.insights import generate_insights
from src.llm_engine import generate_ai_response

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="InsightForge AI",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# TOP LAYOUT: HEADER LEFT + UPLOAD RIGHT
# =========================================================
top_left, top_right = st.columns([1.8, 1])

with top_left:
    st.title("InsightForge AI")
    st.subheader("AI Copilot for Business Data Analysis")
    st.caption(
        "Upload a business dataset, explore its profile, and ask AI-powered analytical questions."
    )

with top_right:
    st.markdown("### Upload Dataset")
    uploaded_file = st.file_uploader(
        "Upload your business dataset (CSV format)",
        type=["csv"],
        label_visibility="collapsed"
    )

st.markdown("---")

# =========================================================
# MAIN APP LOGIC
# =========================================================
if uploaded_file is None:
    st.info("Upload a CSV file to begin exploring your dataset.")

else:
    try:
        # -------------------------
        # LOAD DATA
        # -------------------------
        df = load_csv(uploaded_file)

        # Compact success message
        st.success(f"Loaded dataset: {uploaded_file.name}")

        # -------------------------
        # BACKEND PROCESSING
        # -------------------------
        profile = generate_profile(df)
        insights = generate_insights(profile)

        # =====================================================
        # PAGE LAYOUT: LEFT = DATA WORKSPACE | DIVIDER | RIGHT = AI COPILOT
        # =====================================================
        left_col, divider_col, right_col = st.columns([1.65, 0.03, 1], gap="medium")

        # =====================================================
        # LEFT COLUMN → DATA WORKSPACE
        # =====================================================
        with left_col:
            st.write("## 📊 Data Workspace")

            # -------------------------
            # OVERVIEW METRICS
            # -------------------------
            metric1, metric2, metric3 = st.columns(3)

            metric1.metric("Rows", df.shape[0])
            metric2.metric("Columns", df.shape[1])
            metric3.metric(
                "Missing Values",
                sum(profile["missing_values"].values())
            )

            st.markdown("### Dataset Snapshot")

            # Preview inside expander
            with st.expander("Preview first 10 rows", expanded=True):
                st.dataframe(df.head(10), use_container_width=True)

            # Column names inside expander
            with st.expander("View column names", expanded=False):
                st.write(", ".join(list(df.columns)))

            # -------------------------
            # PROFILE + INSIGHTS TABS
            # -------------------------
            st.markdown("### Analysis Panels")
            tab1, tab2 = st.tabs(["📈 Profile", "🧠 Insights"])

            with tab1:
                st.write("#### Data Profile")

                st.markdown("**Missing Values**")
                missing_df = {
                    "Column": list(profile["missing_values"].keys()),
                    "Missing Count": list(profile["missing_values"].values())
                }
                st.dataframe(missing_df, use_container_width=True)

                st.markdown("**Data Types**")
                dtype_df = {
                    "Column": list(profile["data_types"].keys()),
                    "Data Type": list(profile["data_types"].values())
                }
                st.dataframe(dtype_df, use_container_width=True)

                st.metric("Duplicate Rows", profile["duplicate_rows"])

                st.markdown("**Numeric Summary**")
                st.dataframe(profile["numeric_summary"], use_container_width=True)

            with tab2:
                st.write("#### AI-Generated Dataset Insights")
                for point in insights:
                    st.info(point)

        # =====================================================
        # MIDDLE COLUMN → VERTICAL DIVIDER
        # =====================================================
        with divider_col:
            st.markdown(
                """
                <div style="
                    border-left: 1px solid #3a3a3a;
                    height: 2300px;
                    margin: auto;
                "></div>
                """,
                unsafe_allow_html=True
            )

        # =====================================================
        # RIGHT COLUMN → AI COPILOT PANEL
        # =====================================================
        with right_col:
            st.write("## 🤖 InsightForge Copilot")
            st.caption(
                "Ask questions about your dataset or use quick AI actions for instant analysis."
            )

            # -------------------------
            # QUICK AI ACTIONS
            # -------------------------
            st.markdown("### Quick AI Actions")

            quick_query = None

            if st.button("📌 Summarize Dataset", use_container_width=True):
                quick_query = "Summarize this dataset for a business user."

            if st.button("🧹 Check Data Quality", use_container_width=True):
                quick_query = "Is this dataset clean and ready for analysis?"

            if st.button("📈 Business Insights", use_container_width=True):
                quick_query = "What are the top business insights from this dataset?"

            if st.button("🔍 What Should I Analyze Next?", use_container_width=True):
                quick_query = "What should I analyze next in this dataset?"

            st.markdown("### Ask Your Own Question")

            user_query = st.text_area(
                "Ask a question about your dataset",
                height=120,
                placeholder="Example: Which areas of this dataset need the most business attention?",
                label_visibility="collapsed"
            )

            ask_button = st.button("Ask InsightForge AI", use_container_width=True)

            # -------------------------
            # RUN AI RESPONSE
            # -------------------------
            final_query = None

            if quick_query:
                final_query = quick_query
            elif ask_button and user_query.strip():
                final_query = user_query.strip()

            if final_query:
                with st.spinner("InsightForge AI is analyzing your dataset..."):
                    response = generate_ai_response(final_query, profile)

                st.markdown("### AI Response")
                st.markdown(response)

    except Exception as e:
        st.error(f"Error: {e}")