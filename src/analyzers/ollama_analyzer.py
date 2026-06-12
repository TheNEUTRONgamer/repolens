import json
import requests


def analyze_readme_with_ollama(
    readme_content: str,
    ollama_url: str,
    model: str,
    language: str = "English",
) -> dict:

    prompt = f"""
You are a senior open-source maintainer and developer advocate.

Analyze the repository README and return ONLY valid JSON.

IMPORTANT RULES:
- Output MUST be valid JSON.
- Do NOT include markdown.
- Do NOT use ```json blocks.
- Do NOT explain your answer.
- Do NOT write any text before or after the JSON.

Language: {language}

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

Requirements:

title:
- Project name.

summary:
- 3-5 sentences.

architecture:
- Explain major modules, workflows and technologies.

tech_stack:
- List languages, frameworks, databases, cloud services, CI/CD tools and testing tools.

difficulty:
- Must be EXACTLY one of:
  Beginner
  Intermediate
  Advanced

health_score:
- Must be in format:
  "8/10"
  "9/10"
  "10/10"

components:
- List important project components.

roadmap:
- Create a contributor onboarding roadmap.

tasks:
- Suggest beginner-friendly contribution tasks.

README:

{readme_content[:10000]}
"""

    response = requests.post(
        f"{ollama_url}/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
        },
        timeout=120,
    )

    response.raise_for_status()

    import re

    text = response.json()["response"].strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            return json.loads(match.group(0))

    raise
