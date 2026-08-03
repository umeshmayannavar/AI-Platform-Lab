"""
Application configuration.
"""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class LiteLLMSettings:
    """
    LiteLLM configuration.
    """

    base_url: str = os.getenv(
        "LITELLM_URL",
        "http://localhost:4000",
    )

    api_key: str = os.getenv(
        "LITELLM_API_KEY",
        "ai-platform-lab",
    )


@dataclass(frozen=True)
class QdrantSettings:
    """
    Qdrant configuration.
    """

    host: str = os.getenv(
        "QDRANT_HOST",
        "localhost",
    )

    port: int = int(
        os.getenv(
            "QDRANT_PORT",
            "6333",
        )
    )

    collection: str = os.getenv(
        "QDRANT_COLLECTION",
        "documents",
    )


@dataclass(frozen=True)
class OllamaSettings:
    """
    Ollama runtime configuration.
    """

    base_url: str = os.getenv(
        "OLLAMA_URL",
        "http://localhost:11434",
    )


@dataclass(frozen=True)
class ModelSettings:
    """
    Model aliases exposed by LiteLLM.
    """

    chat: str = os.getenv(
        "CHAT_MODEL",
        "chat",
    )

    embedding: str = os.getenv(
        "EMBEDDING_MODEL",
        "embedding",
    )


@dataclass(frozen=True)
class RetrievalSettings:
    """
    Retrieval configuration.
    """

    top_k: int = int(
        os.getenv(
            "RETRIEVAL_TOP_K",
            "3",
        )
    )


@dataclass(frozen=True)
class Settings:
    """
    Root application settings.
    """

    litellm: LiteLLMSettings = LiteLLMSettings()
    qdrant: QdrantSettings = QdrantSettings()
    ollama: OllamaSettings = OllamaSettings()
    models: ModelSettings = ModelSettings()
    retrieval: RetrievalSettings = RetrievalSettings()


settings = Settings()