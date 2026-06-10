import re
import requests


def fetch_readme_from_url(repo_url: str) -> str:
    """
    Fetches the README.md content from a public GitHub repository URL.

    Args:
        repo_url: The URL of the GitHub repository.

    Returns:
        The text content of the README.md file, or an error message string
        if fetching fails.
    """
    # Regex to extract owner/repo from various GitHub URL formats
    match = re.match(r"https?://github\.com/([\w.-]+)/([\w.-]+)", repo_url)
    if not match:
        raise ValueError("Invalid GitHub repository URL")

    owner, repo = match.groups()

    # Clean up repo name if it ends with .git
    if repo.endswith(".git"):
        repo = repo[:-4]

    # Try fetching from 'main' and then 'master' branch, as these are the most common defaults.
    for branch in ["main", "master"]:
        readme_url = (
            f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/README.md"
        )
        try:
            response = requests.get(readme_url, timeout=10)
            if response.status_code == 200:
                return response.text
            # If we get a 404, we'll just continue to the next branch in the loop.
        except requests.exceptions.RequestException as e:
            raise RuntimeError(
                f"A network error occurred while fetching the README: {e}"
            ) from e

    raise RuntimeError(
        "Could not find a README.md file in the 'main' or 'master' branch "
        "of the repository."
    )
