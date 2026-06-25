"""RepoLens Streamlit application."""

import streamlit as st
from src.analyzers.gemini_analyzer import analyze_readme_with_gemini
from src.analyzers.repo_analyzer import analyze_readme
from src.utils.report_generator import display_report
from src.utils.repository_fetcher import fetch_readme_from_url
from src.analyzers.ollama_analyzer import analyze_readme_with_ollama

st.set_page_config(page_title="RepoLens", page_icon="🔍")

language = st.selectbox(
    "Language / భాష",
    ["English", "తెలుగు"],
)

if language == "తెలుగు":
    APP_TITLE = "🔍 రెపోలెన్స్"
    APP_SUBTITLE = "ఓపెన్ సోర్స్ రిపోజిటరీ ఆన్‌బోర్డింగ్ అసిస్టెంట్"

    PROVIDER_LABEL = "AI ప్రొవైడర్"
    API_KEY_LABEL = "Gemini API కీ (BYOK)"
    API_KEY_HELP = "మీ Gemini API కీని నమోదు చేయండి"

    REPO_LABEL = "రిపోజిటరీ URL (ఐచ్చికం)"
    REPO_PLACEHOLDER = "https://github.com/owner/repo"

    ANALYZE_BUTTON = "రిపోజిటరీని విశ్లేషించు"

    EMPTY_ERROR = "రిపోజిటరీ URL ఇవ్వండి."

    FETCHING_TEXT = "డేటాను తెచ్చి విశ్లేషిస్తోంది..."
    GEMINI_SUCCESS = "Gemini AI విశ్లేషణ ఉపయోగించబడింది"
    COMPLETE_SUCCESS = "విశ్లేషణ పూర్తయింది!"

    FALLBACK_WARNING = "రూల్-బేస్డ్ విశ్లేషకాన్ని ఉపయోగిస్తోంది"

else:
    APP_TITLE = "🔍 RepoLens"
    APP_SUBTITLE = "Open Source Repository Onboarding Assistant"

    PROVIDER_LABEL = "AI Provider"
    API_KEY_LABEL = "Gemini API Key (BYOK)"
    API_KEY_HELP = "Enter your own Gemini API key"

    REPO_LABEL = "Repository URL (Optional)"
    REPO_PLACEHOLDER = "https://github.com/owner/repo"

    ANALYZE_BUTTON = "Analyze Repository"

    EMPTY_ERROR = "Provide either a repository URL."

    FETCHING_TEXT = "Fetching and analyzing..."
    GEMINI_SUCCESS = "Gemini AI analysis used"
    COMPLETE_SUCCESS = "Analysis Complete!"

    FALLBACK_WARNING = "Using fallback rule-based analyzer"

st.title(APP_TITLE)
st.subheader(APP_SUBTITLE)

ai_provider = st.selectbox(
    PROVIDER_LABEL,
    ["Ollama (Local)", "Gemini API (BYOK)"],
)

api_key = None
readme_content = ""
ollama_url = ""
ollama_model = ""

if ai_provider == "Gemini API (BYOK)":
    api_key = st.text_input(
        API_KEY_LABEL,
        type="password",
        help=API_KEY_HELP,
    )

if ai_provider == "Ollama (Local)":
    ollama_url = st.text_input(
        "Ollama URL",
        value="http://localhost:11434",
    )

    ollama_model = st.text_input(
        "Ollama Model",
        value="mistral:latest",
    )

repo_url = st.text_input(
    REPO_LABEL,
    placeholder=REPO_PLACEHOLDER,
)

if st.button(ANALYZE_BUTTON):
    try:
        with st.spinner(FETCHING_TEXT):
            if repo_url.strip():
                readme_content = fetch_readme_from_url(repo_url)
            else:
                st.error(EMPTY_ERROR)
                st.stop()

            if ai_provider == "Gemini API (BYOK)":
                try:
                    analysis_data = analyze_readme_with_gemini(
                        readme_content,
                        api_key,
                        language,
                    )
                    st.success(GEMINI_SUCCESS)

                except Exception as exc:  # pylint: disable=broad-exception-caught
                    st.error(f"Gemini failed: {exc}")
                    analysis_data = analyze_readme(readme_content)
                    st.warning(FALLBACK_WARNING)

            else:
                analysis_data = analyze_readme_with_ollama(
                    readme_content,
                    ollama_url,
                    ollama_model,
                    language,
                )
                st.success(f"Ollama analysis used ({ollama_model})")

        st.success(COMPLETE_SUCCESS)
        display_report(analysis_data)

    except Exception as exc:  # pylint: disable=broad-exception-caught
        st.error(str(exc))
