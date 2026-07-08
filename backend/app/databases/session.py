from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
)

from app.database.engine import engine

###############################################################################
# Session Factory
###############################################################################
SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    # Do not expire ORM objects after commit.
    expire_on_commit=False,
    # Flush changes only when explicitly requested.
    autoflush=False,
    # SQLAlchemy 2.x always uses explicit transactions.
    autocommit=False,
)


# Dependency function that provides a database session for each request
async def get_db_session() -> AsyncGenerator[AsyncSession]:
    # Create a new asynchronous database session.
    # The session will automatically be cleaned up when the block exits.
    async with SessionLocal() as session:
        try:
            # Pause here and provide the session to the FastAPI endpoint.
            # The endpoint uses this session to perform database operations.
            yield session

            # If the endpoint completes successfully,
            # save (commit) all database changes.
            await session.commit()

        except Exception:
            # If any exception occurs while processing the request,
            # undo all uncommitted database changes.
            await session.rollback()

            # Re-raise the exception so FastAPI can handle it
            # (e.g., return an appropriate error response).
            raise

        finally:
            # Always close the session, regardless of success or failure,
            # to release the database connection back to the pool.
            await session.close()


"""
Execution flow
Request arrives
       │
       ▼
Create AsyncSession
       │
       ▼
yield session ─────────────► FastAPI endpoint executes
                                 │
                  ┌──────────────┴──────────────┐
                  │                             │
             Success                      Exception
                  │                             │
                  ▼                             ▼
        session.commit()             session.rollback()
                  │                             │
                  └──────────────┬──────────────┘
                                 ▼
                         session.close()
                                 │
                                 ▼
                      Response / Error returned
"""
