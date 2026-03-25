from fastapi.testclient import TestClient

from fastapi_simple.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "app": "fastapi-simple"}


def test_greet_default():
    response = client.get("/greet")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}


def test_greet_custom():
    response = client.get("/greet", params={"name": "Dharm"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Dharm!"}
