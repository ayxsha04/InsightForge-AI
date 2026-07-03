import os
from dotenv import load_dotenv
import google.generativeai as genai

# =========================================================
# LOAD GEMINI API KEY FROM .env FILE
# =========================================================

# Load environment variables from .env file
load_dotenv()

# Read Gemini API key from the .env file
API_KEY = os.getenv("GEMINI_API_KEY")

# Safety check: stop execution if the key is missing
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini using the API key
genai.configure(api_key=API_KEY)

# Use Gemini Flash model for fast responses
MODEL_NAME = "models/gemini-2.5-flash"
model = genai.GenerativeModel(MODEL_NAME)


# =========================================================
# AI DATA ANALYST FUNCTION
# =========================================================
def generate_ai_response(user_query, profile):
    """
    Generate an AI response using:
    1. the dataset profile
    2. the user's question

    Parameters:
        user_query (str): User's question about the dataset
        profile (dict): Generated dataset profile from profiler.py

    Returns:
        str: AI-generated answer
    """

    prompt = f"""
You are InsightForge AI, a senior business data analyst assistant.

You are given:
1. A dataset profile
2. A user question about the dataset

Your job is to answer ONLY using the dataset profile provided.

IMPORTANT RULES:
- Do NOT invent any values, columns, trends, or facts not present in the profile
- If something cannot be determined from the profile, clearly say that
- Keep the answer business-friendly, simple, and useful
- Focus on data quality, patterns, risks, business insights, and next steps
- Avoid overly technical jargon
- Be concise but insightful

RESPONSE FORMAT:
Always structure your answer in the following format:

## Answer Summary
Give a short direct answer to the user's question.

## Key Findings
Provide 3–5 bullet points based only on the dataset profile.

## Risks / Issues
Mention any data quality problems, unusual values, limitations, or concerns relevant to the question.
If none are obvious, say "No major issues identified from the available profile."

## Recommended Next Steps
Suggest 2–4 meaningful next analyses or actions the user should take based on the dataset.

DATASET PROFILE:
{profile}

USER QUESTION:
{user_query}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Gemini Error: {e}"