"""
Semantic retrieval service.
"""

from ai_platform.config import settings

from ai_platform.embeddings import EmbeddingClient
from ai_platform.vector_store import VectorStore


class RetrievalService:
    """
    Retrieves the most relevant document chunks
    for a natural language question.
    """

    def __init__(
        self,
        embedding_client: EmbeddingClient,
        vector_store: VectorStore,
    ):
        self.embedding_client = embedding_client
        self.vector_store = vector_store

    def retrieve(
        self,
        question: str,
        top_k: int | None = None,
    ) -> list[dict]:
        """
        Retrieve the most relevant chunks for a question.

        If ``top_k`` is not provided, the default configured
        retrieval limit from application settings is used.
        """

        embedding = self.embedding_client.embed(
            question
        )

        return self.vector_store.search(
            embedding,
            limit=top_k or settings.retrieval.top_k,
        )