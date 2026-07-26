"""
Search API models.
"""

from pydantic import BaseModel
from pydantic import Field


class SearchRequest(BaseModel):
    """
    Semantic search request.
    """

    query: str = Field(
        ...,
        min_length=1,
        description="Search query.",
    )

    top_k: int = Field(
        default=3,
        ge=1,
        le=20,
    )


class SearchMatch(BaseModel):
    """
    One semantic search result.
    """

    score: float
    text: str
    source: str
    chunk_id: int


class SearchResponse(BaseModel):
    """
    Search response.
    """

    matches: list[SearchMatch]