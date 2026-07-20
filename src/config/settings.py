"""
Application configuration.
"""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    litellm_url: str = os.getenv(
        "LITELLM_URL",
        "http://localhost:4000",
    )

    litellm_api_key: str = os.getenv(
        "LITELLM_API_KEY",
        "ai-platform-lab",
    )

    qdrant_url: str = os.getenv(
        "QDRANT_URL",
        "http://localhost:6333",
    )


settings = Settings()