from dataclasses import dataclass

from sqlalchemy import URL

from app.config.settings import get_settings

settings = get_settings()


@dataclass(frozen=True)
class DatabaseConfig:
    """
    Immutable database configuration.

    This class centralizes all database-related configuration
    and provides a SQLAlchemy URL object for engine creation.
    """

    host: str
    port: int
    database: str
    username: str
    password: str

    echo: bool

    pool_size: int
    max_overflow: int
    pool_timeout: int
    pool_recycle: int

    @property
    def url(self) -> URL:
        """
        Returns a SQLAlchemy URL object.
        """

        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        )


def get_database_config() -> DatabaseConfig:
    """
    Returns the application's database configuration.

    This function reads the database settings from the application
    configuration and creates an immutable DatabaseConfig object.

    Keeping the configuration creation inside a function improves
    testability and avoids module-level initialization.
    """

    # Load the application settings from settings.py
    settings = get_settings()

    return DatabaseConfig(
        # PostgreSQL server hostname or IP address
        host=settings.database_host,
        # PostgreSQL server port (default: 5432)
        port=settings.database_port,
        # Name of the PostgreSQL database to connect to
        database=settings.database_name,
        # Username used for database authentication
        username=settings.database_user,
        # Password used for database authentication
        password=settings.database_password,
        # Enable SQL query logging.
        # Should be False in production to avoid logging sensitive data.
        echo=settings.database_echo,
        # Number of persistent database connections maintained
        # in the SQLAlchemy connection pool.
        pool_size=settings.database_pool_size,
        # Maximum number of temporary connections that can be
        # created when the connection pool is exhausted.
        max_overflow=settings.database_max_overflow,
        # Maximum number of seconds to wait for an available
        # database connection before raising a TimeoutError.
        pool_timeout=settings.database_pool_timeout,
        # Recycle database connections after this many seconds.
        # Helps prevent failures caused by stale or idle connections.
        pool_recycle=settings.database_pool_recycle,
    )
