from ai_platform.embeddings import EmbeddingService
from ai_platform.vector_store import VectorStore


class Retriever:
    """
    Retrieve relevant document chunks
    from Qdrant.
    """

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def retrieve(
        self,
        question: str,
        limit: int = 3,
    ) -> list[dict]:

        embedding = self.embedding_service.embed(
            question
        )

        return self.vector_store.search(
            embedding,
            limit=limit,
        )