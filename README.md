# InsightForge AI

**AI Copilot for Business Data Analysis**

A Streamlit-based GenAI application that helps users analyze business datasets faster by combining automatic dataset profiling, AI-generated insights, and a Gemini-powered chat assistant in a single dashboard.

Upload a CSV file, get an instant overview of your data quality and structure, then ask questions in plain English to understand what the data is telling you.

## Overview

Business analysis usually starts with the same repetitive steps: checking how big the dataset is, hunting for missing values and duplicates, and figuring out what to look at next. This project automates that first pass and adds an AI assistant on top, so users can go from a raw CSV to actionable insights without writing any code.

The application:

- Accepts business datasets in CSV format through a web interface
- Profiles the dataset (rows, columns, missing values, duplicate rows)
- Previews the uploaded data and lists its columns
- Generates numeric summaries for numerical columns
- Produces AI-generated business insights using the Google Gemini API
- Answers free-form questions about the dataset through a chat assistant
- Offers one-click quick actions for common analysis tasks

> **Note:** This project is a GenAI prototype built for learning and portfolio purposes. AI-generated insights should be verified before being used for real business decisions.

## How It Works

The analysis pipeline follows these steps:

```text
CSV Upload (Streamlit)
     │
     ▼
Load Data (Pandas)
     │
     ▼
Dataset Profiling
     │   ├── Rows / columns
     │   ├── Missing values
     │   ├── Duplicate rows
     │   └── Numeric summaries
     │
     ▼
Dashboard Display (preview, columns, metrics)
     │
     ▼
User Question or Quick Action
     │
     ▼
Prompt with Dataset Context → Gemini API
     │
     ▼
AI Response Displayed in the Dashboard
```

### Dataset Profiling

Pandas handles the structural analysis locally: counting rows and columns, detecting missing values and duplicate rows, and computing summary statistics for numeric columns.

### AI Analysis

The dataset context and the user's request are sent to the Gemini API, which returns business insights, data-quality observations, or answers to specific questions.

## Features

- CSV dataset upload
- Dataset overview: number of rows, number of columns, and missing values
- Data preview and column listing
- Duplicate row detection
- Numeric summaries for numerical columns
- AI-generated business insights
- Gemini-powered chat assistant for dataset-related questions
- Quick AI actions for common analysis tasks

### Quick AI Actions

| Action | Purpose |
|--------|---------|
| Summarize Dataset | Get a plain-language overview of what the dataset contains |
| Check Data Quality | Identify missing values, duplicates, and other data issues |
| Business Insights | Surface key patterns and takeaways relevant to the business |
| What Should I Analyze Next? | Get suggestions for the next analysis steps |

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Streamlit | Web application and user interface |
| Pandas | Data loading, profiling, and summary statistics |
| Google Gemini API | AI-generated insights and chat assistant |
| python-dotenv | Loading the API key from environment variables |

## Project Structure

```text
InsightForge-AI/
│
├── app.py
│   └── Streamlit application, dataset profiling, and Gemini integration
│
├── requirements.txt
│   └── Project dependencies
│
├── .env
│   └── Local environment variables (Gemini API key, not committed)
│
├── .gitignore
│   └── Files and folders excluded from version control
│
└── README.md
    └── Project documentation
```

## Installation

### 1. Clone the Repository

```powershell
git clone https://github.com/ayxsha04/InsightForge-AI.git
cd InsightForge-AI
```

### 2. Create a Virtual Environment

Using a virtual environment is recommended to keep project dependencies isolated.

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\Activate.ps1
```

If activation is successful, your terminal will show:

```text
(venv)
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure the Gemini API Key

Create a `.env` file in the project root and add your key:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

## Usage

Start the application from the project folder:

```powershell
python -m streamlit run app.py
```

Streamlit serves the app at `http://localhost:8501` by default.

The application workflow:

1. Upload a business dataset in CSV format
2. Review the dataset overview, data preview, columns, and numeric summaries
3. Click a quick AI action or type your own question in the chat assistant
4. Read the AI-generated response and continue asking follow-up questions

### Example Questions

- Is this dataset clean and ready for analysis?
- What are the top business insights from this dataset?
- Which parts of the data need the most attention?
- What should I analyze next?

## Configuration

The application is configured through environment variables in the `.env` file:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

### `GEMINI_API_KEY`

The API key used to authenticate requests to the Google Gemini API. The AI insights and the chat assistant will not work without a valid key.

## Requirements

- Python 3.x
- Packages listed in `requirements.txt`
- A Google Gemini API key
- An internet connection for AI features

## Limitations

This implementation is intentionally lightweight and has several limitations:

- Only CSV files are supported.
- AI features require an internet connection and a valid Gemini API key.
- Dataset information is sent to the Gemini API for analysis, so sensitive or confidential data should not be uploaded.
- AI-generated insights can be incomplete or inaccurate and should be verified against the data.
- Dataset profiling covers basic checks (size, missing values, duplicates, numeric summaries) and does not include advanced statistical analysis.
- Very large datasets may be slow to load and analyze.

## Future Improvements

Potential extensions include:

- Support for Excel and other file formats
- Interactive charts and data visualizations
- Correlation analysis and outlier detection
- Automated data-cleaning suggestions
- Exportable analysis reports
- Persistent chat history
- Multi-dataset comparison
- Cloud deployment (Streamlit Cloud or Hugging Face Spaces)
