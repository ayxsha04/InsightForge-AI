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
# HEADER
# =========================================================
st.title("InsightForge AI")
st.subheader("GenAI-Powered Visual Analytics Copilot for Business Data")

st.markdown("---")

# =========================================================
# FILE UPLOAD
# =========================================================
uploaded_file = st.file_uploader(
    "Upload your business dataset (CSV format)",
    type=["csv"]
)

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
        st.success("File uploaded successfully!")

        # -------------------------
        # BACKEND PROCESSING
        # -------------------------
        profile = generate_profile(df)
        insights = generate_insights(profile)

        # =====================================================
        # TABS UI
        # =====================================================
        tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Profile", "🧠 Insights"])

        # -------------------------
        # TAB 1: OVERVIEW
        # -------------------------
        with tab1:
            st.write("## 📊 Dataset Overview")

            col1, col2, col3 = st.columns(3)

            col1.metric("Rows", df.shape[0])
            col2.metric("Columns", df.shape[1])
            col3.metric(
                "Missing Values",
                sum(profile["missing_values"].values())
            )

            st.markdown("---")

            st.write("### Preview")
            st.dataframe(df.head(10), use_container_width=True)

            st.write("### Columns")
            st.write(", ".join(list(df.columns)))

        # -------------------------
        # TAB 2: PROFILE
        # -------------------------
        with tab2:
            st.write("## 📈 Data Profile")

            st.markdown("### Missing Values")
            st.dataframe(profile["missing_values"].items())

            st.markdown("### Data Types")
            st.dataframe(profile["data_types"].items())

            st.metric("Duplicate Rows", profile["duplicate_rows"])

            st.markdown("### Numeric Summary")
            st.dataframe(profile["numeric_summary"], use_container_width=True)

        # -------------------------
        # TAB 3: INSIGHTS
        # -------------------------
        with tab3:
            st.write("## 🧠 AI Insights")

            for point in insights:
                st.info(point)

        # =====================================================
        # 💬 AI CHAT SECTION (IMPORTANT FIXED PART)
        # =====================================================
        st.markdown("---")
        st.write("## 💬 AI Data Analyst Chat")

        user_query = st.text_input("Ask a question about your dataset")

        if user_query:
            with st.spinner("AI is thinking..."):
                response = generate_ai_response(user_query, profile)
                st.success(response)

    except Exception as e:
        st.error(f"Error: {e}")