import streamlit as st

st.set_page_config(page_title="RepoLens")

st.title("🔍 RepoLens")
st.subheader("Open Source Repository Onboarding Assistant")

repo_url = st.text_input("Repository URL")

readme_content = st.text_area(
    "Repository README",
    height=300,
)

if st.button("Analyze Repository"):
    if not readme_content.strip():
        st.error("Please provide README content.")
    else:
        st.success("Repository analyzed!")

        st.markdown("## Project Summary")
        st.write("Placeholder summary")

        st.markdown("## Architecture Overview")
        st.write("Placeholder architecture")

        st.markdown("## Key Components")
        st.write("Placeholder components")

        st.markdown("## Contribution Roadmap")
        st.write("Placeholder roadmap")

        st.markdown("## Beginner-Friendly Tasks")
        st.write("Placeholder tasks")