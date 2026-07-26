"""
Integration tests for Chat API.
"""

from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_chat():

    response = client.post(
        "/chat",
        json={
            "prompt": "Say hello.",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert "response" in body
    assert isinstance(body["response"], str)


def test_chat_validation():

    response = client.post(
        "/chat",
        json={
            "prompt": "",
        },
    )

    assert response.status_code == 422