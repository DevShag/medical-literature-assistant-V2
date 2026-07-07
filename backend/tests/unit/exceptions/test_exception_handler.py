from fastapi import APIRouter, FastAPI
from fastapi.testclient import TestClient

from app.exceptions.custom_exceptions import ApplicationException
from app.exceptions.handlers import application_exception_handler

app = FastAPI()

app.add_exception_handler(
    ApplicationException,
    application_exception_handler,
)

router = APIRouter()


@router.get("/error")
def error():
    raise ApplicationException(
        message="Example Error",
        error_code="EXAMPLE_ERROR",
        status_code=400,
    )


app.include_router(router)

client = TestClient(app)


def test_application_exception_handler():
    response = client.get("/error")

    assert response.status_code == 400

    body = response.json()

    assert body["success"] is False
    assert body["error"]["code"] == "EXAMPLE_ERROR"
    assert body["error"]["message"] == "Example Error"
