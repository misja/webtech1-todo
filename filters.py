import humanize
from models import TaskType
from datetime import datetime, UTC


def type_to_name(value: str) -> str:
    """Return a task name by value"""
    return TaskType(value).name


def time_from_now(date: datetime | None) -> str:
    """Return a human readable time delta"""
    if date:
        # datetime should be timezone aware
        if not date.tzinfo:
            date = date.replace(tzinfo=UTC)

        return humanize.precisedelta(
            date - datetime.now(UTC),
            suppress=["hours", "minutes", "seconds"],
            format="%0.0f",
        )
    return ""
