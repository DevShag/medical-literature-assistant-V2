import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    """
    Shared FastAPI test client for all tests.
    """
    return TestClient(app)
