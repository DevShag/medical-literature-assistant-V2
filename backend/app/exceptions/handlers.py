from datetime import UTC, datetime

from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import ApplicationException


async def application_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    assert isinstance(exc, ApplicationException)

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "request_id": getattr(
                request.state,
                "request_id",
                None,
            ),
            "timestamp": datetime.now(UTC).isoformat(),
            "error": {
                "code": exc.error_code,
                "message": exc.message,
            },
        },
    )
