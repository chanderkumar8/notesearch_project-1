from pathlib import Path

from flask import Flask, render_template, request

from notesearch.indexer import build_index, load_notes, tokenize
from notesearch.search import make_snippet, search

NOTES_FOLDER = Path(__file__).parent / "notes"

app = Flask(__name__)

notes = load_notes(NOTES_FOLDER)
index = build_index(notes)


@app.route("/")
def home():
    query = request.args.get("q", "").strip()
    results = []

    if query:
        query_words = tokenize(query)
        for filename, score in search(query, index):
            results.append({
                "filename": filename,
                "score": score,
                "snippet": make_snippet(notes[filename], query_words),
            })

    return render_template(
        "index.html",
        query=query,
        results=results,
        note_count=len(notes),
    )


if __name__ == "__main__":
    app.run(debug=True)