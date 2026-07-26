"""
Observability middleware.
"""

import logging
import time

from fastapi import Request

from ai_platform.observability.metrics import REQUEST_COUNT
from ai_platform.observability.metrics import REQUEST_DURATION
from ai_platform.observability.metrics import REQUEST_ERRORS

logger = logging.getLogger("ai_platform")


async def observability_middleware(
    request: Request,
    call_next,
):
    """
    Record request metrics and structured logs.
    """

    start = time.perf_counter()

    try:
        response = await call_next(request)

    except Exception:

        REQUEST_ERRORS.labels(
            method=request.method,
            path=request.url.path,
        ).inc()

        logger.exception(
            "Unhandled exception",
            extra={
                "method": request.method,
                "path": request.url.path,
                "client": (
                    request.client.host
                    if request.client
                    else None
                ),
            },
        )

        raise

    duration = time.perf_counter() - start

    REQUEST_COUNT.labels(
        method=request.method,
        path=request.url.path,
        status=response.status_code,
    ).inc()

    REQUEST_DURATION.labels(
        method=request.method,
        path=request.url.path,
    ).observe(duration)

    logger.info(
        "Request completed",
        extra={
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "duration_ms": round(duration * 1000, 2),
            "client": (
                request.client.host
                if request.client
                else None
            ),
        },
    )

    return response