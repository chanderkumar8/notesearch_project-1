# NoteSearch

A small search engine for text and markdown notes, built in Python.
It builds an inverted index of all notes and ranks results by word frequency.

![NoteSearch screenshot](docs/screenshot.png)

## Features
- Inverted index for fast lookup
- Stop-word removal and punctuation cleaning
- Ranked results with text snippets
- Command-line and Flask web interfaces
- Unit tests with pytest

## Run it

    python -m pip install -r requirements.txt
    python app.py

Then open http://127.0.0.1:5000

For the command-line version, run `python main.py`.
##Tests

    python -m pytest

## What I learned
- How an inverted index makes search fast compared with scanning every file
- One design decision: the index is built once at startup, not on every search
