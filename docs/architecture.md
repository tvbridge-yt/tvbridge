# Architecture

TVBridge is a small Python package plus a curated catalog. There is no server,
no database, and no daemon. The "broadcast" is a publishing convention layered
on top of plain dataclasses.

## Pieces

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

## Episode publishing flow

```mermaid
sequenceDiagram
    participant Editor
    participant Catalog
    participant Validator
    participant Renderer
    participant Channels

    Editor->>Catalog: add ResearchTopic / BroadcastEpisode
    Catalog->>Validator: validate_catalog(topics)
    Validator-->>Editor: list of problems (or empty)
    Editor->>Renderer: render_topic_card(topic)
    Renderer->>Channels: publish to docs site, X, telegram
    Channels-->>Editor: ack
```

## Why dataclasses

The catalog is small and hand-curated. We do not want a database or a
schema migration story. Frozen dataclasses give us:

- a single source of truth in Python
- cheap validation in `__post_init__`
- easy diffs in pull requests
- straightforward import from any docs generator

## Channels

| Channel    | Color   | Cadence       | Audience           |
|------------|---------|---------------|--------------------|
| zk         | red     | weekly        | proof system nerds |
| bridge     | blue    | weekly        | interop engineers  |
| anchor     | gold    | bi-weekly     | general            |
| open-docs  | green   | continuous    | researchers        |
<!-- rev 0 -->
<!-- rev 4 -->
<!-- rev 8 -->
<!-- rev 12 -->
<!-- rev 16 -->
<!-- rev 20 -->
<!-- rev 24 -->
<!-- rev 28 -->
<!-- rev 32 -->
<!-- rev 36 -->
<!-- rev 40 -->
<!-- rev 44 -->
<!-- rev 48 -->
<!-- rev 52 -->
