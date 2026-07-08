"""
Base SQLAlchemy model.

Every ORM model in the application inherits from BaseModel.
"""

from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy ORM models.
    """

    pass


class BaseModel(Base):
    """
    Abstract base model.

    Provides common fields shared by every table.
    """

    """
    Without:

    __abstract__ = True

    SQLAlchemy would create a table called: base_model

    We don't want that. This class exists only to be inherited.
    """
    __abstract__ = True

    ###########################################################################
    # Primary Key
    ###########################################################################

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    ###########################################################################
    # Audit Fields
    ###########################################################################

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False,
    )
