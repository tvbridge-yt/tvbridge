"""Curated catalog of research topics."""
from tvbridge.core.topic import ResearchTopic

TOPICS: dict[str, ResearchTopic] = {}


def _add(topic: ResearchTopic) -> None:
    if topic.slug in TOPICS:
        raise ValueError(f"duplicate topic slug: {topic.slug}")
    TOPICS[topic.slug] = topic


_add(ResearchTopic(
    slug="plonk",
    title="PLONK: universal SNARK with KZG commitments",
    channel="zk",
    summary="Universal trusted setup, custom gates, plookup extensions.",
    tags=("snark", "kzg", "universal-setup"),
    references=("https://eprint.iacr.org/2019/953",),
    difficulty=4,
))

_add(ResearchTopic(
    slug="groth16",
    title="Groth16: pairing-based zk-SNARK",
    channel="zk",
    summary="Trusted-setup pairing SNARK with constant-size proofs.",
    tags=("snark", "pairings", "trusted-setup"),
    references=("https://eprint.iacr.org/2016/260",),
    difficulty=4,
))

_add(ResearchTopic(
    slug="stark",
    title="STARKs: hash-based, transparent proofs",
    channel="zk",
    summary="No trusted setup, post-quantum friendly, larger proofs.",
    tags=("stark", "fri", "transparent"),
    references=("https://eprint.iacr.org/2018/046",),
    difficulty=4,
))

_add(ResearchTopic(
    slug="recursive-proofs",
    title="Recursive proof composition",
    channel="zk",
    summary="Verifying proofs inside proofs for unbounded computation.",
    tags=("recursion", "ivc"),
    difficulty=5,
))


def get_topic(slug: str) -> ResearchTopic:
    if slug not in TOPICS:
        raise KeyError(f"unknown topic: {slug}")
    return TOPICS[slug]

_add(ResearchTopic(
    slug="light-clients",
    title="ZK light clients",
    channel="bridge",
    summary="Succinct verification of consensus for trust-minimized bridging.",
    tags=("light-client", "consensus"),
    references=(),
    difficulty=4,
))

_add(ResearchTopic(
    slug="ibc",
    title="IBC: inter-blockchain communication",
    channel="bridge",
    summary="Cosmos-native interoperability protocol with light client verification.",
    tags=("ibc", "cosmos"),
    references=("https://ibcprotocol.org/",),
    difficulty=3,
))

_add(ResearchTopic(
    slug="layerzero-v2",
    title="LayerZero v2 messaging",
    channel="bridge",
    summary="Configurable security stack with DVN and executor split.",
    tags=("messaging", "dvn"),
    references=("https://layerzero.network/",),
    difficulty=2,
))

_add(ResearchTopic(
    slug="hyperlane-isms",
    title="Hyperlane interchain security modules",
    channel="bridge",
    summary="Permissionless interoperability with pluggable ISMs.",
    tags=("messaging", "ism"),
    references=("https://hyperlane.xyz/",),
    difficulty=3,
))

_add(ResearchTopic(
    slug="wormhole-vaa",
    title="Wormhole guardian VAAs",
    channel="bridge",
    summary="Verified action approvals signed by the guardian set.",
    tags=("messaging", "guardians"),
    references=("https://wormhole.com/",),
    difficulty=2,
))

_add(ResearchTopic(
    slug="axelar-amplifier",
    title="Axelar Amplifier",
    channel="bridge",
    summary="GMP routing layer with verifier sets per chain.",
    tags=("messaging", "gmp"),
    references=("https://www.axelar.network/",),
    difficulty=3,
))

_add(ResearchTopic(
    slug="zkvm-sp1",
    title="SP1 zkVM",
    channel="zk",
    summary="RISC-V based zkVM from Succinct Labs.",
    tags=("zkvm", "risc-v", "sp1"),
    references=("https://github.com/succinctlabs/sp1",),
    difficulty=3,
))

_add(ResearchTopic(
    slug="zkvm-risc0",
    title="RISC Zero zkVM",
    channel="zk",
    summary="General purpose RISC-V zkVM with continuations.",
    tags=("zkvm", "risc-v", "risc0"),
    references=("https://www.risczero.com/",),
    difficulty=3,
))
