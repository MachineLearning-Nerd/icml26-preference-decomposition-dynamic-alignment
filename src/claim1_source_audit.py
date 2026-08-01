from pathlib import Path

def test_pinned_theorem_text():
    t=(Path(__file__).parents[1]/'evidence/source/theorem45_excerpt.tex').read_text().lower()
    assert 'orthogonal' in t and 'unique' in t
