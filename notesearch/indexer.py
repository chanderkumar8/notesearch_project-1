import re
from collections import Counter, defaultdict
from pathlib import Path

STOP_WORDS = {
    "a", "an", "the", "is", "are", "was", "were", "and", "or", "of",
    "to", "in", "on", "for", "it", "its", "this", "that", "with", "as",
    "by", "at", "be", "from", "into", "over", "until", "inside",
}


def load_notes(folder):
    """Read every .txt and .md file in a folder. Returns {filename: text}."""
    notes = {}
    for path in sorted(Path(folder).glob("*")):
        if path.suffix in {".txt", ".md"}:
            notes[path.name] = path.read_text(encoding="utf-8")
    return notes


def tokenize(text):
    """Turn text into a list of lowercase words, without stop words."""
    words = re.findall(r"[a-z0-9]+", text.lower())
    return [word for word in words if word not in STOP_WORDS]


def build_index(notes):
    """Build an inverted index: {word: {filename: count}}."""
    index = defaultdict(dict)
    for filename, text in notes.items():
        counts = Counter(tokenize(text))
        for word, count in counts.items():
            index[word][filename] = count
    return index