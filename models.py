from enum import Enum
from datetime import datetime, UTC
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class TaskType(Enum):
    EASY = "Easy"
    BORING = "Boring"
    HARD = "Hard"


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
    type: Mapped[TaskType] = mapped_column(default=TaskType.EASY)
    completed: Mapped[bool] = mapped_column(default=True)
    deadline: Mapped[datetime]
