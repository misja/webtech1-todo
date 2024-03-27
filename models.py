from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, UTC

db = SQLAlchemy()


class TimestampModel(db.Model):
    __abstract__ = True
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )


class Task(TimestampModel):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    type: Mapped[int] = mapped_column(default=1)
    complete: Mapped[bool] = mapped_column(default=True)
    deadline: Mapped[datetime]
