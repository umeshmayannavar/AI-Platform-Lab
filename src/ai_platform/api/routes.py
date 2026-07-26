"""
API routes for AI Platform Lab.
"""

from fastapi import APIRouter
from fastapi import HTTPException

from ai_platform.api.models import (
    ChatRequest,
    ChatResponse,
    RAGRequest,
    RAGResponse,
)
from ai_platform.embeddings import EmbeddingClient
from ai_platform.llm import chat
from ai_platform.rag import (
    ContextBuilder,
    RAGService,
)
from ai_platform.retrieval.service import RetrievalService
from ai_platform.vector_store import VectorStore

router = APIRouter()


@router.get("/")
def root():
    """
    Root endpoint.
    """

    return {
        "name": "AI Platform Lab",
        "version": "0.1.0",
        "status": "running",
    }


@router.get("/health")
def health():
    """
    Liveness probe.
    """

    return {
        "status": "healthy",
    }


@router.get("/ready")
def ready():
    """
    Readiness probe.
    """

    return {
        "status": "ready",
    }


@router.post(
    "/chat",
    response_model=ChatResponse,
    tags=["Chat"],
)
def chat_endpoint(
    request: ChatRequest,
) -> ChatResponse:
    """
    Generate a response using the configured LLM.
    """

    try:

        response = chat(
            request.prompt,
        )

        return ChatResponse(
            response=response,
        )

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


@router.post(
    "/rag",
    response_model=RAGResponse,
    tags=["RAG"],
)
def rag_endpoint(
    request: RAGRequest,
) -> RAGResponse:
    """
    Generate an answer using Retrieval-Augmented Generation.
    """

    try:

        embedding_client = EmbeddingClient()

        vector_store = VectorStore()

        retrieval = RetrievalService(
            embedding_client,
            vector_store,
        )

        context_builder = ContextBuilder()

        rag = RAGService(
            retrieval_service=retrieval,
            context_builder=context_builder,
        )

        answer = rag.answer(
            request.question,
        )

        return RAGResponse(
            answer=answer,
        )

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )