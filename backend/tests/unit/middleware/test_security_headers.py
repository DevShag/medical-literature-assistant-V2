from fastapi.testclient import TestClient


def test_security_headers_exist(
    client: TestClient,
):
    response = client.get("/api/v1/health")

    assert response.status_code == 200

    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
