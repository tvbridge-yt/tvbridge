"""Validation rules for ResearchTopic entries and the curated catalog."""
from __future__ import annotations

from typing import Iterable, List

from tvbridge.core.topic import ResearchTopic, CHANNELS
from tvbridge.utils.slugify import slugify


def validate_topic(topic: ResearchTopic) -> List[str]:
    """Return a list of human-readable problems with this topic."""
    problems: List[str] = []

    if topic.channel not in CHANNELS:
        problems.append(f"{topic.slug}: unknown channel {topic.channel!r}")

    if slugify(topic.title) and topic.slug != slugify(topic.title):
        pass  # soft hint, slugs can be hand-curated

    if len(topic.summary) < 10:
        problems.append(f"{topic.slug}: summary is too short")

    if len(topic.summary) > 240:
        problems.append(f"{topic.slug}: summary is too long")

    if topic.difficulty < 1 or topic.difficulty > 5:
        problems.append(f"{topic.slug}: difficulty out of range")

    return problems


def validate_catalog(topics: Iterable[ResearchTopic]) -> List[str]:
    problems: List[str] = []
    seen: set[str] = set()
    for t in topics:
        if t.slug in seen:
            problems.append(f"duplicate slug: {t.slug}")
        seen.add(t.slug)
        problems.extend(validate_topic(t))
    return problems
