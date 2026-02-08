"""Weekly programming schedule."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


WEEKDAYS = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")


@dataclass(frozen=True)
class WeeklySchedule:
    name: str
    slots: tuple[tuple[str, str, str], ...]  # (weekday, time_utc, channel)

    def __post_init__(self) -> None:
        for weekday, time_utc, channel in self.slots:
            if weekday not in WEEKDAYS:
                raise ValueError(f"unknown weekday: {weekday}")
            if len(time_utc) != 5 or time_utc[2] != ":":
                raise ValueError(f"time must be HH:MM, got {time_utc!r}")

    def by_day(self) -> Dict[str, List[tuple[str, str]]]:
        out: Dict[str, List[tuple[str, str]]] = {d: [] for d in WEEKDAYS}
        for weekday, time_utc, channel in self.slots:
            out[weekday].append((time_utc, channel))
        return out
