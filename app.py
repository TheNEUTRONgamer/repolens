import streamlit as st
from src.analyzers.gemini_analyzer import analyze_readme_with_gemini
from src.analyzers.repo_analyzer import analyze_readme
from src.utils.report_generator import display_report
from src.utils.repository_fetcher import fetch_readme_from_url

st.set_page_config(page_title="RepoLens", page_icon="🔍")

st.title("🔍 RepoLens")
st.subheader("Open Source Repository Onboarding Assistant")

ai_provider = st.selectbox(
    "AI Provider",
    ["Ollama (Local)", "Gemini API (BYOK)"],
)

api_key = None

if ai_provider == "Gemini API (BYOK)":
    api_key = st.text_input(
        "Gemini API Key (BYOK)",
        type="password",
        help="Enter your own Gemini API key",
    )

language = st.selectbox(
    "Language / భాష",
    ["English", "తెలుగు"],
)

repo_url = st.text_input(
    "Repository URL (Optional)",
    placeholder="https://github.com/owner/repo",
)

readme_content = st.text_area(
    "Paste Repository README Content Here",
    height=300,
    placeholder="Paste the full content of a repository's README.md file here to get an analysis.",
)

if st.button("Analyze Repository"):
    try:
        with st.spinner("Fetching and analyzing..."):
            if repo_url.strip():
                readme_content = fetch_readme_from_url(repo_url)

            if not readme_content.strip():
                st.error("Provide either a repository URL or README content.")
                st.stop()

            if ai_provider == "Gemini API (BYOK)":
                try:
                    analysis_data = analyze_readme_with_gemini(
                        readme_content,
                        api_key,
                        language,
                    )
                    st.success("Gemini AI analysis used")

                except Exception as e:
                    st.error(f"Gemini failed: {e}")
                    analysis_data = analyze_readme(readme_content)
                    st.warning("Using fallback rule-based analyzer")

            else:
                st.warning(
                    "Ollama integration is being configured. For now, use Gemini API."
                )
                st.stop()

        st.success("Analysis Complete!")
        display_report(analysis_data)

    except Exception as e:
        st.error(str(e))
