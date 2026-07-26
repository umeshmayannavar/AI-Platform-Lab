"""
Embedding client backed by LiteLLM.
"""

from openai import OpenAI

from ai_platform.config import settings


class EmbeddingClient:
    """
    Wrapper around LiteLLM embedding endpoint.
    """

    def __init__(self):

        self.client = OpenAI(
            base_url=f"{settings.litellm.base_url}/",
            api_key=settings.litellm.api_key,
        )

    def embed(
        self,
        text: str,
    ) -> list[float]:

        response = self.client.embeddings.create(
            model=settings.models.embedding,
            input=text,
        )

        return response.data[0].embedding