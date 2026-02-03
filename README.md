![TVBridge](./banner.png)

<h1 align="center">TVBridge</h1>
<p align="center"><em>A VHS-era television channel for ZK proof systems and cross-chain interoperability research.</em></p>

<p align="center">
  <a href="./LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
  <img alt="Python 3.11+" src="https://img.shields.io/badge/python-3.11%2B-3776AB.svg">
  <a href="https://github.com/tvbridge-yt/tvbridge/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/tvbridge-yt/tvbridge/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://twitter.com/tvb_yt"><img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/tvb_yt?style=social"></a>
  <a href="https://tvb.yt"><img alt="Website" src="https://img.shields.io/badge/web-tvb.yt-FF0033.svg"></a>
  <a href="https://github.com/tvbridge-yt/tvbridge/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/tvbridge-yt/tvbridge?style=social"></a>
</p>

TVBridge is the static catalog and Python package behind a VHS-styled
broadcast channel covering zero-knowledge proof systems and cross-chain
interoperability research. Anchor-chan reads the headlines, the topic
catalog feeds the docs site, and the episode catalog drives the schedule.

Think of it as a small reference library that happens to be wrapped in a
broadcast metaphor. Every episode points at one or more curated research
topics, every topic points at primary sources, and every weekly slot maps
to one of four channels.

## What's on the channels

- **ZK channel** - SNARKs, STARKs, recursive proofs, zkVMs.
- **Bridge channel** - light clients, IBC, LayerZero v2, Hyperlane, Wormhole, Axelar.
- **Anchor reports** - long-form weekly summaries from Anchor-chan.
- **Open docs** - working notes, papers under review, half-finished diagrams.

<p align="center"><img src="./banner.png" alt="TVBridge" width="100%"/></p>

## Architecture

```mermaid
graph TD
    A[Anchor-chan] -->|curates| B[Daily Broadcast]
    B --> C[ZK Channel]
    B --> D[Bridge Channel]
    B --> E[Anchor Reports]
    B --> F[Open Docs]
    C --> G[Topic Catalog]
    D --> G
    E --> G
    F --> G
    G --> H[Public Docs Site]
    G --> I[Telegram Alerts]

    classDef red fill:#FF0033,stroke:#fff,color:#fff
    classDef blue fill:#0066FF,stroke:#fff,color:#fff
    classDef gold fill:#FFD700,stroke:#000,color:#000
    classDef green fill:#00FF41,stroke:#000,color:#000
    classDef navy fill:#1A1A2E,stroke:#fff,color:#fff

    class A red
    class B blue
    class C,D,E,F gold
    class G green
    class H,I navy
```

The full version, including the episode publishing flow, lives in
[docs/architecture.md](./docs/architecture.md).

<p align="center"><img src="./banner.png" alt="TVBridge" width="100%"/></p>

## Programming schedule

| Day  | Time UTC | Channel       | Format                |
|------|----------|---------------|-----------------------|
| Mon  | 18:00    | zk            | Topic deep dive       |
| Tue  | 18:00    | bridge        | Topic deep dive       |
| Wed  | 20:00    | open-docs     | Working notes         |
| Thu  | 18:00    | zk            | Paper club            |
| Fri  | 21:00    | anchor        | Anchor-chan recap     |
| Sat  | 16:00    | bridge        | Field guide           |
| Sun  | -        | -             | Off air               |

## Installation

```bash
pip install -e .
```

For development:

```bash
pip install -e .[dev]
pytest -q
```

## Quick start

```python
from tvbridge.catalog import TOPICS, EPISODES
from tvbridge.utils.markdown import render_topic_card

groth16 = TOPICS["groth16"]
print(groth16.title, "-", groth16.channel)

# render a markdown card for the docs site
print(render_topic_card(groth16))

# walk the broadcast schedule
for number in sorted(EPISODES):
    ep = EPISODES[number]
    print(ep.code, ep.air_date, ep.title)
```

There are runnable examples under `src/examples/`:

```bash
python src/examples/list_topics.py
python src/examples/list_episodes.py
```

## Project structure

```
src/tvbridge/
  core/         dataclasses for episodes, topics, schedules
  catalog/      curated topic and episode catalog
  validators/   catalog validation rules
  utils/        slugify and markdown helpers
src/examples/   small runnable scripts
tests/          pytest suite
docs/           architecture and per-topic briefs
```

## Contributing

See [docs/contributing.md](./docs/contributing.md). Topic proposals go
through the issue template; small fixes can come straight as a pull
request.

## Links

- Website: [tvb.yt](https://tvb.yt)
- X: [@tvb_yt](https://twitter.com/tvb_yt)
- GitHub: [tvbridge-yt/tvbridge](https://github.com/tvbridge-yt/tvbridge)
- Ticker: $TVB
<!-- rev 3 -->
<!-- rev 7 -->
<!-- rev 11 -->
<!-- rev 15 -->
<!-- rev 19 -->
<!-- rev 23 -->
<!-- rev 27 -->
<!-- rev 31 -->
<!-- rev 35 -->
<!-- rev 39 -->
<!-- rev 43 -->
<!-- rev 47 -->
<!-- rev 51 -->
