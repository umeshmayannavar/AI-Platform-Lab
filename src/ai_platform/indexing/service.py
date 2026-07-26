"""
Document indexing service.
"""

from pathlib import Path

from ai_platform.chunking import chunk_text
from ai_platform.embeddings import EmbeddingClient
from ai_platform.loader import load_document
from ai_platform.vector_store import VectorStore


class IndexingService:
    """
    Loads, chunks, embeds and indexes documents.
    """

    def __init__(
        self,
        embedding_client: EmbeddingClient,
        vector_store: VectorStore,
    ):
        self.embedding_client = embedding_client
        self.vector_store = vector_store

    def index_document(
        self,
        path: str,
    ) -> int:
        """
        Index a single document.

        Returns:
            Number of chunks indexed.
        """

        document = load_document(path)

        chunks = chunk_text(
            document.content,
            Path(path),
        )

        if not chunks:
            return 0

        first_embedding = self.embedding_client.embed(
            chunks[0].text,
        )

        self.vector_store.create_collection(
            vector_size=len(first_embedding),
        )

        self.vector_store.upsert(
            chunks[0],
            first_embedding,
        )

        for chunk in chunks[1:]:

            embedding = self.embedding_client.embed(
                chunk.text,
            )

            self.vector_store.upsert(
                chunk,
                embedding,
            )

        return len(chunks)