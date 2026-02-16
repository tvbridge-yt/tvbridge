import pytest

from tvbridge.core.topic import ResearchTopic


def _make(**overrides):
    base = dict(
        slug="groth16",
        title="Groth16",
        channel="zk",
        summary="A pairing-based zk-SNARK with constant-size proofs.",
        tags=("snark",),
        difficulty=4,
    )
    base.update(overrides)
    return ResearchTopic(**base)


def test_topic_basic_fields():
    t = _make()
    assert t.slug == "groth16"


def test_topic_rejects_unknown_channel():
    with pytest.raises(ValueError):
        _make(channel="television")


def test_topic_requires_slug():
    with pytest.raises(ValueError):
        _make(slug="")


def test_topic_has_tag_is_case_insensitive():
    t = _make(tags=("SNARK", "Pairings"))
    assert t.has_tag("snark")
    assert t.has_tag("pairings")
    assert not t.has_tag("stark")
