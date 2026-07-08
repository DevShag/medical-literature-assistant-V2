from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
)

from app.config.database import get_database_config

database_config = get_database_config()

engine: AsyncEngine = create_async_engine(
    database_config.url,
    echo=database_config.echo,
    pool_size=database_config.pool_size,
    max_overflow=database_config.max_overflow,
    pool_timeout=database_config.pool_timeout,
    pool_recycle=database_config.pool_recycle,
    pool_pre_ping=True,
)
