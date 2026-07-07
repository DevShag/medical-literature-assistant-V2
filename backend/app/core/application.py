from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.config.logging import configure_logging
from app.config.settings import get_settings
from app.core.lifespan import lifespan
from app.exceptions.custom_exceptions import ApplicationException
from app.exceptions.handlers import application_exception_handler
from app.middleware.logging import LoggingMiddleware
from app.middleware.request_id import RequestIDMiddleware
from app.middleware.security import SecurityHeadersMiddleware


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

    app.add_exception_handler(
        ApplicationException,
        application_exception_handler,
    )

    app.add_middleware(SecurityHeadersMiddleware)
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(RequestIDMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=settings.allow_credentials,
        allow_methods=settings.allowed_methods,
        allow_headers=settings.allowed_headers,
    )
    """
    print("\nRegistered middleware:")
    for m in app.user_middleware:
        print(m.cls.__name__)
    """

    return app
