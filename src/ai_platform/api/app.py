"""
FastAPI application.
"""

from fastapi import FastAPI

from ai_platform.api.routes import router


def create_app() -> FastAPI:
    """
    Application factory.
    """

    app = FastAPI(
        title="AI Platform Lab",
        description="Production-ready AI Platform built with LiteLLM, Qdrant and FastAPI.",
        version="0.1.0",
    )

    app.include_router(router)

    return app


app = create_app()