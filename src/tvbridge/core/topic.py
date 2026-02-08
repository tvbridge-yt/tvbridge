"""Research topic dataclass.

A ResearchTopic represents a single subject the broadcast covers,
roughly corresponding to one segment in an episode.
"""
from __future__ import annotations

from dataclasses import dataclass, field

CHANNELS = ("zk", "bridge", "anchor", "open-docs")


@dataclass(frozen=True)
class ResearchTopic:
    slug: str
    title: str
    channel: str
    summary: str
    tags: tuple[str, ...] = field(default_factory=tuple)
    references: tuple[str, ...] = field(default_factory=tuple)
    difficulty: int = 2

    def __post_init__(self) -> None:
        if self.channel not in CHANNELS:
            raise ValueError(
                f"channel must be one of {CHANNELS}, got {self.channel!r}"
            )
        if not 1 <= self.difficulty <= 5:
            raise ValueError("difficulty must be in 1..5")
        if not self.slug:
            raise ValueError("slug is required")
        if not self.title:
            raise ValueError("title is required")

    def has_tag(self, tag: str) -> bool:
        return tag.lower() in (t.lower() for t in self.tags)
