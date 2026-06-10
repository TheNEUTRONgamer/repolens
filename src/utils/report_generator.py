import streamlit as st
from typing import Dict, List, Union


def display_report(analysis_results: Dict[str, Union[str, List[str]]]) -> None:
    """
    Renders the full analysis report in the Streamlit interface.

    Args:
        analysis_results: The dictionary returned by analyze_readme.
    """
    title = str(analysis_results.get("title", "RepoLens Analysis"))
    if title and title != "No Title Found":
        st.header(title)

    # --- Project Summary ---
    st.subheader("📄 Project Summary")
    summary = str(analysis_results.get("summary", ""))
    if summary and "not found" not in summary.lower():
        st.write(summary)
    else:
        st.info("A project summary could not be generated from the README.")

    # --- Architecture Overview ---
    st.subheader("🏗️ Architecture Overview")
    architecture = str(analysis_results.get("architecture", ""))
    if architecture and "not found" not in architecture.lower():
        st.write(architecture)
    else:
        st.info("An architecture overview was not found in the README.")

    # --- Key Components ---
    st.subheader("🧩 Key Components")
    components = analysis_results.get("components", [])
    if isinstance(components, list) and components:
        # Filter out generic fallback messages
        if "Components not identified" not in components[0]:
            for component in components:
                st.markdown(f"- {component}")
        else:
            st.info("No specific components were listed or detected in the README.")
    else:
        st.info("No specific components were listed or detected in the README.")

    # --- Contribution Roadmap ---
    st.subheader("🗺️ Contribution Roadmap")
    roadmap = analysis_results.get("roadmap", [])
    if isinstance(roadmap, list) and roadmap:
        # Check for default values before printing
        if "Read project documentation" not in roadmap[0]:
            for i, step in enumerate(roadmap, 1):
                st.markdown(f"{i}. {step}")
        else:
            st.info("A generic contribution roadmap is suggested:")
            for i, step in enumerate(roadmap, 1):
                st.markdown(f"{i}. {step}")
    else:
        st.info("No contribution roadmap was found in the README.")

    # --- Beginner-Friendly Tasks ---
    st.subheader("✅ Beginner-Friendly Tasks")
    tasks = analysis_results.get("tasks", [])
    if isinstance(tasks, list) and tasks:
        # Check for default values before printing
        if "Improve documentation" not in tasks[0]:
            for task in tasks:
                st.markdown(f"- {task}")
        else:
            st.info("Generic contribution tasks are suggested:")
            for task in tasks:
                st.markdown(f"- {task}")
    else:
        st.info("No beginner-friendly tasks were found in the README.")
