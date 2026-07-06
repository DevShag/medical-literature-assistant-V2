from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from app.config.environment import Environment

class Settings(BaseSettings):
    app_name: str = "Medical Literature Assistant"

    environment: Environment = Environment.DEVELOPMENT

    debug: bool = True

    api_v1_prefix: str = "/api/v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()   