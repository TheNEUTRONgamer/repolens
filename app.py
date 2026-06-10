import streamlit as st
from src.analyzers.repo_analyzer import analyze_readme
from src.utils.report_generator import display_report

st.set_page_config(page_title="RepoLens", page_icon="🔍")

st.title("🔍 RepoLens")
st.subheader("Open Source Repository Onboarding Assistant")

readme_content = st.text_area(
    "Paste Repository README Content Here",
    height=300,
    placeholder="Paste the full content of a repository's README.md file here to get an analysis.",
)

if st.button("Analyze Repository"):
    if not readme_content.strip():
        st.error("Please provide README content to analyze.")
    else:
        with st.spinner("Analyzing..."):
            # 1. Call the analyzer
            analysis_data = analyze_readme(readme_content)

        st.success("Analysis Complete!")

        # 2. Call the report generator to display the results
        display_report(analysis_data)