from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_security_headers_exist():
    response = client.get("/api/v1/health")

    assert response.status_code == 200

    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
