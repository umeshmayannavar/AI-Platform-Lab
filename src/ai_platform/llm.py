"""
LLM service abstraction.

All application code should use LLMService instead of
calling LiteLLM directly.
"""

from openai import OpenAI

from ai_platform.config import settings


class LLMService:
    """
    Service responsible for LLM interactions.

    Currently backed by LiteLLM using the OpenAI-compatible API.
    """

    def __init__(self):
        self.client = OpenAI(
            base_url=f"{settings.litellm.base_url}/",
            api_key=settings.litellm.api_key,
        )

    def generate(
        self,
        prompt: str,
        model: str | None = None,
    ) -> str:
        """
        Generate a response from the configured LLM.
        """

        response = self.client.chat.completions.create(
            model=model or settings.models.chat,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content