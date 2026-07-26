"""
API routes for AI Platform Lab.
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from ai_platform.api.dependencies import (
    get_llm_service,
    get_rag_service,
)

from ai_platform.api.models import (
    ChatRequest,
    ChatResponse,
    RAGRequest,
    RAGResponse,
)

from ai_platform.llm import LLMService
from ai_platform.rag import RAGService


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
    llm_service: LLMService = Depends(get_llm_service),
) -> ChatResponse:

    try:

        response = llm_service.generate(
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
    rag_service: RAGService = Depends(get_rag_service),
) -> RAGResponse:

    try:

        answer = rag_service.answer(
            request.question,
        )

        return RAGResponse(
            answer=answer,
        )

    except Exception as exc:

        print(f"RAG Error: {exc}")

        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )