"""
Integration tests for health endpoints.
"""

from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "AI Platform Lab"
    assert data["status"] == "running"


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "healthy",
    }


def test_ready():

    response = client.get("/ready")

    assert response.status_code == 200

    assert response.json() == {
        "status": "ready",
    }