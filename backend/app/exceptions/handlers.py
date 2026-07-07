from datetime import datetime

from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import ApplicationException


async def application_exception_handler(
    request: Request,
    exc: ApplicationException,
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "request_id": getattr(
                request.state,
                "request_id",
                None,
            ),
            "timestamp": datetime.utcnow().isoformat(),
            "error": {
                "code": exc.error_code,
                "message": exc.message,
            },
        },
    )
