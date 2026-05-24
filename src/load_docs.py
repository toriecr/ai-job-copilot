from src.config import DOCS_DIRS, ROOT


def load_docs() -> list[dict]:
    documents = []

    for docs_dir in DOCS_DIRS:
        doc_type = docs_dir.name

        for md_path in docs_dir.rglob("*.md"):
            text = md_path.read_text(encoding="utf-8")

            if not text.strip():
                continue

            relative_path = md_path.relative_to(ROOT / "docs").as_posix()

            documents.append(
                {
                    "path": relative_path,
                    "text": text,
                    "doc_type": doc_type,
                }
            )

    return documents


if __name__ == "__main__":
    docs = load_docs()
    print(f"Loaded {len(docs)} documents")
    for d in docs:
        print(f" [{d['doc_type']}] {d['path']} ({len(d['text'])} chars)")
