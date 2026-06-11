import json
import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_readme_with_gemini(readme_content: str) -> dict:
    prompt = f"""
You are a senior open-source maintainer and developer advocate.

Your job is to help a new contributor understand and contribute to a repository.

Return ONLY valid JSON.

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
- Example:
  Read README
  Setup development environment
  Run project locally
  Run tests
  Explore codebase
  Fix first issue
  Submit pull request

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
