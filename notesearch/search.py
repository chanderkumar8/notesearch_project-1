import re

from notesearch.indexer import tokenize


def search(query, index):
    """Return [(filename, score), ...] sorted from best to worst match."""
    scores = {}
    for word in tokenize(query):
        for filename, count in index.get(word, {}).items():
            scores[filename] = scores.get(filename, 0) + count
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)


def make_snippet(text, query_words, width=60):
    """Return a short piece of text around the first matching word."""
    lowered = text.lower()
    for word in query_words:
        match = re.search(r"\b" + re.escape(word) + r"\b", lowered)
        if match:
            start = max(0, match.start() - width)
            end = min(len(text), match.end() + width)
            snippet = text[start:end].replace("\n", " ")
            prefix = "..." if start > 0 else ""
            suffix = "..." if end < len(text) else ""
            return prefix + snippet + suffix
    return text[:width * 2].replace("\n", " ")