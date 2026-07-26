"""
RAG API request/response models.
"""

from pydantic import BaseModel
from pydantic import Field


class RAGRequest(BaseModel):
    """
    RAG request.
    """

    question: str = Field(
        ...,
        min_length=1,
        description="Question to ask the knowledge base.",
        examples=[
            "What is Kubernetes?",
        ],
    )


class RAGResponse(BaseModel):
    """
    RAG response.
    """

    answer: str