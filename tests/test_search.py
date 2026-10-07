from notesearch.indexer import build_index, tokenize
from notesearch.search import search


def test_tokenize_lowercases_and_removes_punctuation():
    assert tokenize("Hello, World!") == ["hello", "world"]


def test_tokenize_removes_stop_words():
    assert tokenize("the loop is fast") == ["loop", "fast"]


def test_build_index_counts_words():
    notes = {"a.txt": "loop loop code", "b.txt": "code"}
    index = build_index(notes)
    assert index["loop"] == {"a.txt": 2}
    assert index["code"] == {"a.txt": 1, "b.txt": 1}


def test_search_ranks_higher_count_first():
    notes = {"a.txt": "loop", "b.txt": "loop loop loop"}
    results = search("loop", build_index(notes))
    assert results[0][0] == "b.txt"


def test_search_unknown_word_returns_empty():
    index = build_index({"a.txt": "loop"})
    assert search("banana", index) == []


def test_search_empty_query_returns_empty():
    index = build_index({"a.txt": "loop"})
    assert search("", index) == []