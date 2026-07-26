"""
API routes for AI Platform Lab.
"""

from fastapi import APIRouter
from fastapi import HTTPException

from ai_platform.api.models import (
    ChatRequest,
    ChatResponse,
)
from ai_platform.llm import chat

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
    Generate a chat response using LiteLLM.
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