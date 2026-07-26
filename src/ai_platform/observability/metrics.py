"""
Prometheus metrics for AI Platform Lab.
"""

from prometheus_client import CONTENT_TYPE_LATEST
from prometheus_client import Counter
from prometheus_client import Histogram
from prometheus_client import generate_latest


REQUEST_COUNT = Counter(
    "ai_platform_requests_total",
    "Total HTTP requests",
    [
        "method",
        "path",
        "status",
    ],
)


REQUEST_ERRORS = Counter(
    "ai_platform_request_errors_total",
    "Total failed HTTP requests",
    [
        "method",
        "path",
    ],
)


REQUEST_DURATION = Histogram(
    "ai_platform_request_duration_seconds",
    "HTTP request duration",
    [
        "method",
        "path",
    ],
)


def metrics_response() -> tuple[bytes, str]:
    """
    Return Prometheus metrics payload.
    """

    return (
        generate_latest(),
        CONTENT_TYPE_LATEST,
    )