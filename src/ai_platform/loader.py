from pathlib import Path

from ai_platform.types import Document


SUPPORTED_EXTENSIONS = {
    ".md",
    ".txt",
}


def load_document(path: str | Path) -> Document:
    """
    Load a text document.
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