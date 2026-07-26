"""
API routes for AI Platform Lab.
"""

from fastapi import APIRouter

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