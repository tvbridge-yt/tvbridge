from tvbridge.catalog import TOPICS
from tvbridge.validators import validate_catalog, validate_topic
from tvbridge.core.topic import ResearchTopic


def test_curated_catalog_is_clean():
    problems = validate_catalog(TOPICS.values())
    assert problems == [], problems


def test_validator_flags_short_summary():
    t = ResearchTopic(
        slug="x",
        title="X",
        channel="zk",
        summary="too short",
        difficulty=2,
    )
    problems = validate_topic(t)
    assert any("too short" in p for p in problems)
