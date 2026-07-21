from ai_platform.types import Chunk


def chunk_text(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 200,
) -> list[Chunk]:
    """
    Split text into overlapping chunks.
    """

    chunks = []

    start = 0
    chunk_id = 1

    while start < len(text):

        end = start + chunk_size

        chunks.append(
            Chunk(
                id=chunk_id,
                text=text[start:end],
            )
        )

        start += chunk_size - overlap
        chunk_id += 1

    return chunks