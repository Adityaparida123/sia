import os
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv

SERVICES_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(dotenv_path=SERVICES_ROOT / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")


def ask_chatbot(prompt):
    response = model.generate_content(prompt)
    return response.text
