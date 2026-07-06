# InsightForge AI

## AI Copilot for Business Data Analysis
InsightForge AI is a Streamlit-based GenAI project that helps users analyze business datasets more efficiently.  
It combines dataset profiling, AI-generated insights, and a Gemini-powered chat assistant in one dashboard.


## Features
- Upload business datasets in **CSV format**
- View dataset overview:
  - number of rows
  - number of columns
  - missing values
- Preview uploaded data
- View column names
- Detect duplicate rows
- Generate numeric summaries for numerical columns
- Get AI-generated business insights
- Ask dataset-related questions using **Gemini AI**
- Use quick AI actions like:
  - **Summarize Dataset**
  - **Check Data Quality**
  - **Business Insights**
  - **What Should I Analyze Next?**


## Tech Stack
- **Python**
- **Streamlit**
- **Pandas**
- **Google Gemini API**
- **python-dotenv**


Installation & Setup
1. Clone the repository
git clone https://github.com/ayxsha04/InsightForge-AI.git
cd InsightForge-AI

3. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

5. Install dependencies
pip install -r requirements.txt

7. Create a .env file in the project root
GEMINI_API_KEY=your_actual_gemini_api_key_here

8. Run the app
python -m streamlit run app.py


## Example Questions to Ask
- Is this dataset clean and ready for analysis?
- What are the top business insights from this dataset?
- Which parts of the data need the most attention?
- What should I analyze next?
