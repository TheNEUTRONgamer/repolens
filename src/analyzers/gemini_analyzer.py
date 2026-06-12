import json
import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

DEFAULT_API_KEY = os.getenv("GEMINI_API_KEY")


def analyze_readme_with_gemini(
    readme_content: str,
    api_key: str | None = None,
    language: str = "English",
) -> dict:
    key = api_key or DEFAULT_API_KEY

    if not key:
        raise ValueError("No Gemini API key provided")

    genai.configure(api_key=key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
You are a senior open-source maintainer and developer advocate.

Your job is to help a new contributor understand and contribute to a repository.

Return ONLY valid JSON.

Language: {language}

If language is Telugu:
- Write summary in Telugu.
- Write architecture in Telugu.
- Write roadmap in Telugu.
- Write tasks in Telugu.

Schema:

{{
  "title": "",
  "summary": "",
  "architecture": "",
  "tech_stack": [],
  "difficulty": "",
  "health_score": "",
  "components": [],
  "roadmap": [],
  "tasks": []
}}

Instructions:

title:
- Project name.

summary:
- Explain what the project does.
- 3-5 sentences.
- Written for a new contributor.

architecture:
- Explain the system architecture.
- Mention important modules, layers, workflows, and technologies.

tech_stack:
- List programming languages.
- List frameworks.
- List databases.
- List cloud platforms.
- List CI/CD tools.
- List testing frameworks.

difficulty:
- Choose EXACTLY ONE:
  Beginner
  Intermediate
  Advanced

health_score:
- Give a score out of 10.
- Example:
  "8/10"
- Provide a short justification.
- Consider:
  Documentation quality
  Repository organization
  Contributor friendliness
  Ease of onboarding
  Presence of contribution guidelines
  Codebase complexity

components:
- List the most important project components.

roadmap:
- Create a realistic onboarding roadmap.

tasks:
- Suggest realistic beginner-friendly contribution tasks.

Return JSON only.
Do not include markdown.
Do not include explanations outside JSON.

README:

{readme_content[:15000]}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)
