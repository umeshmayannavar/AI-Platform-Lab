from dataclasses import dataclass
from pathlib import Path


@dataclass
class Document:
    """
    Represents a document loaded from disk.
    """

    path: Path
    content: str


@dataclass
class Chunk:
    """
    Represents one chunk of a document.
    """

    id: int
    text: str