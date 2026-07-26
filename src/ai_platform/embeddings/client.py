"""
Embedding client backed by LiteLLM.

All embedding requests should go through this client instead of
calling Ollama directly.
"""

from openai import OpenAI


DEFAULT_BASE_URL = "http://localhost:4000"
DEFAULT_API_KEY = "ai-platform-lab"
DEFAULT_MODEL = "embedding"


class EmbeddingClient:
    """
    Wrapper around LiteLLM embedding endpoint.
    """

    def __init__(
        self,
        base_url: str = DEFAULT_BASE_URL,
        api_key: str = DEFAULT_API_KEY,
        model: str = DEFAULT_MODEL,
    ):
        self.model = model

        self.client = OpenAI(
            base_url=f"{base_url}/",
            api_key=api_key,
        )

    def embed(
        self,
        text: str,
    ) -> list[float]:

        response = self.client.embeddings.create(
            model=self.model,
            input=text,
        )

        return response.data[0].embedding