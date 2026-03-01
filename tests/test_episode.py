from datetime import date

import pytest

from tvbridge.core.episode import BroadcastEpisode


def test_episode_code_is_zero_padded():
    ep = BroadcastEpisode(
        number=7,
        title="IBC field guide",
        air_date=date(2026, 3, 21),
        channel="bridge",
        topic_slugs=("ibc",),
    )
    assert ep.code == "TVB-007"


def test_episode_requires_at_least_one_topic():
    with pytest.raises(ValueError):
        BroadcastEpisode(
            number=1,
            title="Empty",
            air_date=date(2026, 2, 1),
            channel="zk",
            topic_slugs=(),
        )


def test_episode_rejects_zero_runtime():
    with pytest.raises(ValueError):
        BroadcastEpisode(
            number=1,
            title="x",
            air_date=date(2026, 2, 1),
            channel="zk",
            topic_slugs=("groth16",),
            runtime_minutes=0,
        )



def test_catalog_loads():
    from tvbridge.catalog import EPISODES
    from tvbridge.catalog.topics import TOPICS
    assert len(EPISODES) >= 4
    for ep in EPISODES.values():
        for slug in ep.topic_slugs:
            assert slug in TOPICS, f"missing topic referenced by episode: {slug}"
