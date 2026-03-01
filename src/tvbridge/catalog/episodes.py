"""Curated catalog of broadcast episodes."""
from __future__ import annotations

from datetime import date
from typing import Dict

from tvbridge.core.episode import BroadcastEpisode


EPISODES: Dict[int, BroadcastEpisode] = {}


def _add(ep: BroadcastEpisode) -> None:
    if ep.number in EPISODES:
        raise ValueError(f"duplicate episode number: {ep.number}")
    EPISODES[ep.number] = ep


_add(BroadcastEpisode(
    number=1,
    title="Cold open: why a VHS channel for ZK",
    air_date=date(2026, 2, 14),
    channel="anchor",
    topic_slugs=("groth16",),
    runtime_minutes=22,
    notes="Pilot episode. Anchor-chan introduces the broadcast format.",
))

_add(BroadcastEpisode(
    number=2,
    title="Pairing rituals: Groth16 from scratch",
    air_date=date(2026, 2, 21),
    channel="zk",
    topic_slugs=("groth16",),
    runtime_minutes=34,
))

_add(BroadcastEpisode(
    number=3,
    title="PLONK and the universal setup",
    air_date=date(2026, 2, 28),
    channel="zk",
    topic_slugs=("plonk",),
    runtime_minutes=31,
))

_add(BroadcastEpisode(
    number=4,
    title="STARKs and the FRI low-degree dance",
    air_date=date(2026, 3, 7),
    channel="zk",
    topic_slugs=("stark",),
    runtime_minutes=33,
))

_add(BroadcastEpisode(
    number=5,
    title="Recursive proofs without the headache",
    air_date=date(2026, 3, 14),
    channel="zk",
    topic_slugs=("recursive-proofs", "stark"),
    runtime_minutes=29,
))

_add(BroadcastEpisode(
    number=6,
    title="Bridge channel pilot: light clients 101",
    air_date=date(2026, 3, 17),
    channel="bridge",
    topic_slugs=("light-clients",),
    runtime_minutes=27,
))

_add(BroadcastEpisode(
    number=7,
    title="IBC field guide",
    air_date=date(2026, 3, 21),
    channel="bridge",
    topic_slugs=("ibc", "light-clients"),
    runtime_minutes=30,
))

_add(BroadcastEpisode(
    number=8,
    title="LayerZero v2 deep dive",
    air_date=date(2026, 3, 24),
    channel="bridge",
    topic_slugs=("layerzero-v2",),
    runtime_minutes=28,
))

_add(BroadcastEpisode(
    number=9,
    title="Hyperlane and the ISM zoo",
    air_date=date(2026, 3, 28),
    channel="bridge",
    topic_slugs=("hyperlane-isms",),
    runtime_minutes=26,
))

_add(BroadcastEpisode(
    number=10,
    title="Wormhole guardians and VAAs",
    air_date=date(2026, 3, 31),
    channel="bridge",
    topic_slugs=("wormhole-vaa",),
    runtime_minutes=25,
))

_add(BroadcastEpisode(
    number=11,
    title="Axelar Amplifier under the hood",
    air_date=date(2026, 4, 3),
    channel="bridge",
    topic_slugs=("axelar-amplifier",),
    runtime_minutes=27,
))

_add(BroadcastEpisode(
    number=12,
    title="zkVMs side by side: SP1 and RISC Zero",
    air_date=date(2026, 4, 5),
    channel="zk",
    topic_slugs=("zkvm-sp1", "zkvm-risc0"),
    runtime_minutes=36,
))


def get_episode(number: int) -> BroadcastEpisode:
    if number not in EPISODES:
        raise KeyError(f"unknown episode: {number}")
    return EPISODES[number]
