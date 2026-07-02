import google.generativeai as genai

# =========================================================
# 🔑 GEMINI API CONFIG
# =========================================================

API_KEY = "YOUR_GEMINI_API_KEY"

# Configure Gemini
genai.configure(api_key=API_KEY)

# Use a model that is actually available in your account
MODEL_NAME = "models/gemini-2.5-flash"
model = genai.GenerativeModel(MODEL_NAME)


# =========================================================
# 🧠 AI DATA ANALYST FUNCTION
# =========================================================
def generate_ai_response(user_query, profile):
    """
    Generates an AI response using:
    1. dataset profile
    2. user's question
    """

    prompt = f"""
You are a senior data analyst AI assistant.

You are given:
1. A dataset profile
2. A user question about the dataset

Your rules:
- Answer ONLY using the dataset profile provided
- Do NOT invent data that is not present
- Keep the response simple, clear, and business-friendly
- Focus on insights, data quality, trends, patterns, and recommendations
- If the answer cannot be fully determined from the profile, say so honestly

DATASET PROFILE:
{profile}

USER QUESTION:
{user_query}

Now provide a helpful answer.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Gemini Error: {e}"