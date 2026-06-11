import streamlit as st
from typing import Dict, List, Union


def display_report(
    analysis_results: Dict[str, Union[str, List[str]]],
) -> None:
    """
    Renders the full analysis report in the Streamlit interface.
    """

    title = str(
        analysis_results.get(
            "title",
            "RepoLens Analysis",
        )
    )

    if title and title != "No Title Found":
        st.header(title)

    # Summary
    st.subheader("📄 Project Summary")

    summary = str(
        analysis_results.get(
            "summary",
            "",
        )
    )

    if summary:
        st.write(summary)

    # Architecture
    st.subheader("🏗️ Architecture Overview")

    architecture = str(
        analysis_results.get(
            "architecture",
            "",
        )
    )

    if architecture:
        st.write(architecture)

    # Tech Stack
    st.subheader("🛠️ Tech Stack")

    tech_stack = analysis_results.get(
        "tech_stack",
        [],
    )

    if isinstance(tech_stack, list) and tech_stack:
        for tech in tech_stack:
            st.markdown(f"- {tech}")
    else:
        st.info("Tech stack not identified.")

    # Contributor Difficulty
    st.subheader("🎯 Contributor Difficulty")

    difficulty = str(
        analysis_results.get(
            "difficulty",
            "Unknown",
        )
    )

    st.write(difficulty)

    # Repository Health
    st.subheader("📊 Repository Health Score")

    health_score = str(
        analysis_results.get(
            "health_score",
            "N/A",
        )
    )

    st.write(health_score)

    # Components
    st.subheader("🧩 Key Components")

    components = analysis_results.get(
        "components",
        [],
    )

    if isinstance(components, list) and components:
        for component in components:
            st.markdown(f"- {component}")
    else:
        st.info("No components identified.")

    # Roadmap
    st.subheader("🗺️ Contribution Roadmap")

    roadmap = analysis_results.get(
        "roadmap",
        [],
    )

    if isinstance(roadmap, list) and roadmap:
        for i, step in enumerate(
            roadmap,
            start=1,
        ):
            st.markdown(f"{i}. {step}")
    else:
        st.info("No roadmap generated.")

    # Tasks
    st.subheader("✅ Beginner-Friendly Tasks")

    tasks = analysis_results.get(
        "tasks",
        [],
    )

    if isinstance(tasks, list) and tasks:
        for task in tasks:
            st.markdown(f"- {task}")
    else:
        st.info("No beginner-friendly tasks generated.")
