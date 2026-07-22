from pathlib import Path

from ai_platform.types import Document


SUPPORTED_EXTENSIONS = {
    ".md",
    ".txt",
}


def load_document(path: str | Path) -> Document:
    """
    Load a single text document.
    """

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(path)

    if path.suffix not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {path.suffix}"
        )

    return Document(
        path=path,
        content=path.read_text(encoding="utf-8"),
    )


def load_documents(directory: str | Path) -> list[Document]:
    """
    Load all supported documents from a directory recursively.
    """

    directory = Path(directory)

    if not directory.exists():
        raise FileNotFoundError(directory)

    documents: list[Document] = []

    for extension in SUPPORTED_EXTENSIONS:
        for file in directory.rglob(f"*{extension}"):
            documents.append(load_document(file))

    return documents