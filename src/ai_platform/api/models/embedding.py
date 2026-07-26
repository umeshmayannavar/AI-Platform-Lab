"""
Embedding API models.
"""

from pydantic import BaseModel
from pydantic import Field


class EmbeddingRequest(BaseModel):
    """
    Embedding request.
    """

    text: str = Field(
        ...,
        min_length=1,
    )


class EmbeddingResponse(BaseModel):
    """
    Embedding response.
    """

    dimensions: int
    embedding: list[float]