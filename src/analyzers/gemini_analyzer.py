import json
import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_readme_with_gemini(readme_content: str) -> dict:
    prompt = f"""
You are an expert open-source maintainer.

Analyze the following repository README.

Return ONLY valid JSON.

Schema:

{{
  "title": "",
  "summary": "",
  "architecture": "",
  "components": [],
  "roadmap": [],
  "tasks": []
}}

README:

{readme_content[:15000]}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)
