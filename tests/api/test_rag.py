"""
Integration tests for RAG API.
"""

from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_rag():

    response = client.post(
        "/rag",
        json={
            "question": "What is Kubernetes?",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert "answer" in body
    assert isinstance(body["answer"], str)


def test_rag_validation():

    response = client.post(
        "/rag",
        json={
            "question": "",
        },
    )

    assert response.status_code == 422