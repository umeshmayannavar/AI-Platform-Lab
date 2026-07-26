from ai_platform.embeddings import EmbeddingClient
from ai_platform.retrieval.service import RetrievalService
from ai_platform.vector_store import VectorStore


def test_retrieval_service_creation():

    embedding_client = EmbeddingClient()

    vector_store = VectorStore()

    retrieval = RetrievalService(
        embedding_client,
        vector_store,
    )

    assert retrieval is not None