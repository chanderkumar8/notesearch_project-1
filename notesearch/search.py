from notesearch.indexer import tokenize


def search(query, index):
    """Return [(filename, score), ...] sorted from best to worst match."""
    scores = {}
    for word in tokenize(query):
        for filename, count in index.get(word, {}).items():
            scores[filename] = scores.get(filename, 0) + count
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)