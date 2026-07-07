import time

import structlog
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

logger = structlog.get_logger()


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Logs every incoming HTTP request and outgoing response.

    Responsibilities:
    - Measure request latency
    - Emit structured logs
    - Add X-Response-Time response header
    """

    RESPONSE_TIME_HEADER = "X-Response-Time"

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        start_time = time.perf_counter()
        response: Response = await call_next(request)

        latency_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2,
        )

        logger.info(
            "request_completed",
            request_id=getattr(request.state, "request_id", None),
            method=request.method,
            path=request.url.path,
            status_code=response.status_code,
            latency_ms=latency_ms,
            client_ip=request.client.host if request.client else None,
        )

        response.headers[self.RESPONSE_TIME_HEADER] = f"{latency_ms} ms"

        return response
