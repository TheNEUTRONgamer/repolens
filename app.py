import streamlit as st
from src.analyzers.repo_analyzer import analyze_readme
from src.utils.report_generator import display_report
from src.utils.repository_fetcher import fetch_readme_from_url

st.set_page_config(page_title="RepoLens", page_icon="🔍")

st.title("🔍 RepoLens")
st.subheader("Open Source Repository Onboarding Assistant")

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

            analysis_data = analyze_readme(readme_content)

        st.success("Analysis Complete!")

        display_report(analysis_data)

    except Exception as e:
        st.error(str(e))
