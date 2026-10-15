from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root_returns_hello_message():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}


def test_health_returns_healthy_status():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}