"""
LiteLLM client helpers.

All application code should use this module instead of
calling Ollama directly.
"""

from openai import OpenAI

from ai_platform.config import settings


def create_client() -> OpenAI:
    """
    Create an OpenAI-compatible client that points to LiteLLM.
    """

    return OpenAI(
        base_url=f"{settings.litellm.base_url}/",
        api_key=settings.litellm.api_key,
    )


def chat(
    prompt: str,
    model: str | None = None,
) -> str:
    """
    Send a simple chat request.
    """

    client = create_client()

    response = client.chat.completions.create(
        model=model or settings.models.chat,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content