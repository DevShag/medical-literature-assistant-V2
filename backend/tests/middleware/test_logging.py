from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_logging_middleware_does_not_break_request():
    response = client.get("/api/v1/health")

    assert response.status_code == 200