"""Broadcast episode dataclass."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass(frozen=True)
class BroadcastEpisode:
    number: int
    title: str
    air_date: date
    channel: str
    topic_slugs: tuple[str, ...] = field(default_factory=tuple)
    runtime_minutes: int = 30
    notes: str = ""

    def __post_init__(self) -> None:
        if self.number < 1:
            raise ValueError("episode number must be >= 1")
        if self.runtime_minutes <= 0:
            raise ValueError("runtime must be positive")
        if not self.topic_slugs:
            raise ValueError("episode must cover at least one topic")

    @property
    def code(self) -> str:
        return f"TVB-{self.number:03d}"
