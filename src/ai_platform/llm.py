"""
LiteLLM client helpers.

All application code should use this module instead of
calling Ollama directly.
"""

from openai import OpenAI


DEFAULT_BASE_URL = "http://localhost:4000"
DEFAULT_API_KEY = "ai-platform-lab"


def create_client(
    base_url: str = DEFAULT_BASE_URL,
    api_key: str = DEFAULT_API_KEY,
) -> OpenAI:
    """
    Create an OpenAI-compatible client that points to LiteLLM.
    """

    return OpenAI(
        base_url=f"{base_url}/",
        api_key=api_key,
    )


def chat(
    prompt: str,
    model: str = "chat",
) -> str:
    """
    Send a simple chat request.
    """

    client = create_client()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content