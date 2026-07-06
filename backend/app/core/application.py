from fastapi import FastAPI

from app.config.logging import configure_logging
from app.config.settings import get_settings
from app.core.lifespan import lifespan
from app.api.router import api_router
from app.middleware.request_id import RequestIDMiddleware



def create_app() -> FastAPI:
    """
    Application Factory.
    """

    settings = get_settings()

    configure_logging(settings.log_level)

    app = FastAPI(
        title=settings.app_name,
        version="1.0.0",
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )


    app.include_router(
        api_router,
        prefix=settings.api_v1_prefix,
    )

    app.add_middleware(RequestIDMiddleware)

    return app