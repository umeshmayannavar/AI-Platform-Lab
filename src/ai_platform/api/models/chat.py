"""
Chat API request/response models.
"""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Chat request.
    """

    prompt: str = Field(
        ...,
        min_length=1,
        description="User prompt",
        examples=[
            "Explain Kubernetes in simple terms.",
        ],
    )


class ChatResponse(BaseModel):
    """
    Chat response.
    """

    response: str