from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.enums.environment import Environment
from app.enums.log_level import LogLevel


class Settings(BaseSettings):
    """
    Application settings.

    Values are loaded in the following order:
    1. Environment variables
    2. .env file
    3. Default values
    """

    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------

    app_name: str = Field(
        default="Medical Literature Assistant",
        description="Application name",
    )

    app_version: str = Field(
        default="1.0.0",
        description="Application version",
    )

    environment: Environment = Field(
        default=Environment.DEVELOPMENT,
    )

    debug: bool = Field(default=True)

    api_v1_prefix: str = Field(default="/api/v1")

    # Logging
    # ------------------------------------------------------------------
    log_level: str = Field(
        default=LogLevel.INFO,
        description="Logging level",
    )

    # ------------------------------------------------------------------
    # CORS Middleware Configuration
    # ------------------------------------------------------------------
    allowed_origins: list[str] = Field(
        default=[
            "http://localhost:3000",  # React
            "http://localhost:5173",  # Vite
        ]
    )

    allowed_methods: list[str] = Field(
        default=[
            "GET",
            "POST",
            "PUT",
            "PATCH",
            "DELETE",
            "OPTIONS",
        ]
    )

    allowed_headers: list[str] = Field(
        default=[
            "Authorization",
            "Content-Type",
            "X-Request-ID",
        ]
    )

    allow_credentials: bool = True

    # ------------------------------------------------------------------
    # Settings Configuration
    # ------------------------------------------------------------------
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings instance.
    """
    return Settings()
