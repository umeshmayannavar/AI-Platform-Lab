"""
Document API models.
"""

from pydantic import BaseModel
from pydantic import Field


class DocumentRequest(BaseModel):
    """
    Document indexing request.
    """

    path: str = Field(
        ...,
        description="Path to the document to index.",
        examples=[
            "documents/sample.md",
        ],
    )


class DocumentResponse(BaseModel):
    """
    Document indexing response.
    """

    status: str
    chunks: int