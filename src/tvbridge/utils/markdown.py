"""Tiny markdown helpers used by docs generators."""
from __future__ import annotations

from tvbridge.core.topic import ResearchTopic


def render_topic_card(topic: ResearchTopic) -> str:
    """Render a single research topic as a small markdown card."""
    lines = [
        f"### {topic.title}",
        "",
        f"- channel: `{topic.channel}`",
        f"- difficulty: {topic.difficulty}/5",
        f"- tags: {', '.join(topic.tags) if topic.tags else '_none_'}",
        "",
        topic.summary,
    ]
    if topic.references:
        lines.append("")
        lines.append("References:")
        for ref in topic.references:
            lines.append(f"- {ref}")
    return "\n".join(lines).rstrip() + "\n"
