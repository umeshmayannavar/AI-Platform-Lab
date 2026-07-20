"""
Application entry point.
"""

from src.config.settings import settings


def main() -> None:
    print("AI Platform Lab")
    print("================")
    print()

    print(f"LiteLLM : {settings.litellm_url}")
    print(f"Qdrant  : {settings.qdrant_url}")


if __name__ == "__main__":
    main()