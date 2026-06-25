def test_import():
    from src.analyzers.repo_analyzer import analyze_readme

    assert callable(analyze_readme)
