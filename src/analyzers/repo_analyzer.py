import re
from typing import Dict, List

FEATURE_KEYWORDS = [
    "api",
    "frontend",
    "backend",
    "database",
    "authentication",
    "docker",
    "testing",
]


def _parse_section(text: str, heading: str) -> str:
    """
    Extracts content under a specific markdown heading until the next heading.

    Args:
        text: The full text to parse.
        heading: The heading to search for (case-insensitive).

    Returns:
        The content of the section, or an empty string if not found.
    """
    pattern = re.compile(
        rf"^(#+)\s*{re.escape(heading)}\s*\n(.*?)(?=\n\1\s|\Z)",
        re.DOTALL | re.IGNORECASE | re.MULTILINE,
    )
    match = pattern.search(text)
    return match.group(2).strip() if match else ""


def _find_list_items(text: str) -> List[str]:
    """Finds markdown list items in a block of text."""
    if not text:
        return []
    # Matches lines starting with *, -, or a number followed by a period.
    items = re.findall(
        r"^\s*(?:[-*]|\d+\.)\s+(.*)",
        text,
        re.MULTILINE,
    )
    return [item.strip() for item in items]


def _extract_title(text: str) -> str:
    """Extracts the first H1 markdown heading as the title."""
    match = re.search(r"^\s*#\s+(.*)", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def _detect_components(text: str) -> list[str]:
    """Detect common project components from README keywords."""
    detected = []

    lowered = text.lower()

    for keyword in FEATURE_KEYWORDS:
        if keyword in lowered:
            detected.append(keyword.title())

    return detected


def analyze_readme(readme_content: str) -> Dict[str, str | List[str]]:
    """
    Analyzes README content using rule-based methods to extract project information.

    Args:
        readme_content: The raw text content of the repository's README file.

    Returns:
        A dictionary containing the structured analysis results.
    """
    if not readme_content or not readme_content.strip():
        return {
            "title": "No Title Found",
            "summary": "README content was not provided.",
            "architecture": "No content provided.",
            "components": [],
            "roadmap": [],
            "tasks": [],
        }

    title = _extract_title(readme_content)

    summary_section = (
        _parse_section(readme_content, "Description")
        or _parse_section(readme_content, "Overview")
        or _parse_section(readme_content, "Problem Statement")
    )

    architecture_section = _parse_section(readme_content, "Architecture")

    components_section = _parse_section(
        readme_content, "Key Components"
    ) or _parse_section(readme_content, "Features")

    roadmap_section = _parse_section(readme_content, "Roadmap") or _parse_section(
        readme_content, "Getting Started"
    )

    tasks_section = _parse_section(readme_content, "Contributing") or _parse_section(
        readme_content, "Beginner-Friendly Tasks"
    )

    analysis: Dict[str, str | List[str]] = {
        "title": title or "No Title Found",
        "summary": summary_section or title or "Summary not found.",
        "architecture": architecture_section
        or "No dedicated architecture section found in README.",
        "components": (
            _find_list_items(components_section)
            or _detect_components(readme_content)
            or ["Components not identified from README"]
        ),
        "roadmap": _find_list_items(roadmap_section)
        or [
            "Read project documentation",
            "Set up the project locally",
            "Explore source code",
        ],
        "tasks": _find_list_items(tasks_section)
        or ["Improve documentation", "Add tests", "Review open issues"],
    }

    return analysis
