"""
Application entry point.
"""

from fastapi import FastAPI
from fastapi import Response

from ai_platform.api.routes import router
from ai_platform.observability.logging import configure_logging
from ai_platform.observability.metrics import metrics_response
from ai_platform.observability.middleware import observability_middleware

configure_logging()

app = FastAPI(
    title="AI Platform Lab",
    version="0.1.0",
)

app.middleware("http")(observability_middleware)

app.include_router(router)


@app.get(
    "/metrics",
    tags=["Observability"],
)
def metrics():
    """
    Prometheus metrics endpoint.
    """

    data, content_type = metrics_response()

    return Response(
        content=data,
        media_type=content_type,
    )