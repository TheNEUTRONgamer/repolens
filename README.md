# 🔍 RepoLens

AI-powered Open Source Repository Onboarding Assistant.

RepoLens helps developers understand unfamiliar repositories in minutes. Instead of manually reading long README files, users can provide a GitHub repository URL or README content and receive a structured onboarding report generated using Gemini AI.

## Problem

Contributing to open-source projects is difficult because newcomers often spend hours understanding:

* Project purpose
* Architecture
* Tech stack
* Repository structure
* Contribution workflow

This onboarding friction discourages potential contributors.

## Solution

RepoLens automatically analyzes repository documentation and generates:

* 📄 Project Summary
* 🏗️ Architecture Overview
* 🛠️ Tech Stack Detection
* 🎯 Contributor Difficulty Rating
* 📊 Repository Health Score
* 🧩 Key Components
* 🗺️ Contribution Roadmap
* ✅ Beginner-Friendly Tasks

## Features

### Repository URL Analysis

Analyze any public GitHub repository by simply entering its URL.

### AI-Powered Insights

Gemini AI extracts and summarizes repository knowledge into a contributor-friendly format.

### Tech Stack Detection

Automatically identifies frameworks, libraries, languages, tooling, and infrastructure.

### Contributor Guidance

Generates onboarding paths and beginner contribution suggestions.

### Health Scoring

Evaluates documentation quality, project organization, and onboarding friendliness.

## Architecture

```text
User Input
     │
     ▼
GitHub Repository URL
     │
     ▼
README Fetcher
     │
     ▼
Gemini Analyzer
     │
     ▼
Structured JSON Report
     │
     ▼
Streamlit Dashboard
```

## Tech Stack

* Python
* Streamlit
* Gemini API
* Requests
* Ruff
* Mypy
* Pre-commit
* UV

## Installation

```bash
git clone https://github.com/TheNEUTRONgamer/repolens.git
cd repolens

uv sync

uv run streamlit run app.py
```

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

## Usage

### Option 1: Analyze Repository URL

Paste a public GitHub repository URL and click **Analyze Repository**.

### Option 2: Analyze README Content

Paste repository README content directly into the application.

## Live Demo

https://repolens-theneutrongamer.streamlit.app/

## Example Output

RepoLens generates:

* Project Summary
* Architecture Overview
* Tech Stack
* Contributor Difficulty
* Repository Health Score
* Key Components
* Contribution Roadmap
* Beginner-Friendly Tasks

## Future Improvements

* GitHub issue analysis
* Good-first-issue recommendations
* Multi-repository comparison
* Contributor skill matching
* Repository activity analytics

## Contributors

### @TheNEUTRONgamer (indravandith)

* Project architecture
* Streamlit frontend
* Repository fetching
* Gemini integration
* Deployment
* Compliance improvements
* Documentation
