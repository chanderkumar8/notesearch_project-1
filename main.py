from pathlib import Path

from notesearch.indexer import build_index, load_notes
from notesearch.search import search

NOTES_FOLDER = Path(__file__).parent / "notes"


def main():
    notes = load_notes(NOTES_FOLDER)
    if not notes:
        print("No notes found. Add .txt or .md files to the notes folder.")
        return

    index = build_index(notes)
    print(f"Indexed {len(notes)} notes with {len(index)} unique words.")

    while True:
        query = input("\nSearch (or type 'quit'): ").strip()
        if query.lower() == "quit":
            break
        if not query:
            continue

        results = search(query, index)
        if not results:
            print("No results found.")
            continue

        for rank, (filename, score) in enumerate(results, start=1):
            print(f"{rank}. {filename} (score: {score})")


if __name__ == "__main__":
    main()