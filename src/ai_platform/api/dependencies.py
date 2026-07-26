"""
FastAPI dependency providers.
"""

from functools import lru_cache

from ai_platform.embeddings import EmbeddingClient
from ai_platform.rag import (
    ContextBuilder,
    RAGService,
)
from ai_platform.retrieval.service import RetrievalService
from ai_platform.vector_store import VectorStore


@lru_cache()
def get_embedding_client() -> EmbeddingClient:
    return EmbeddingClient()


@lru_cache()
def get_vector_store() -> VectorStore:
    return VectorStore()


@lru_cache()
def get_retrieval_service() -> RetrievalService:

    return RetrievalService(
        embedding_client=get_embedding_client(),
        vector_store=get_vector_store(),
    )


@lru_cache()
def get_rag_service() -> RAGService:

    return RAGService(
        retrieval_service=get_retrieval_service(),
        context_builder=ContextBuilder(),
    )