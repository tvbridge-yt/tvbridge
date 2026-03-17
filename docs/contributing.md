# Contributing

Thanks for considering a contribution. TVBridge is mostly a curated catalog,
so most pull requests are small and self-contained.

## Adding a research topic

1. Open an issue with the `Research topic suggestion` template first, so we
   can agree on the slug and the channel.
2. Add a `ResearchTopic` entry to `src/tvbridge/catalog/topics.py`.
3. Add a short brief to `docs/research-topics/<slug>.md`.
4. Run `pytest -q` locally. The validator test will catch most problems.

## Adding an episode

1. Pick the next free episode number.
2. Reference at least one topic that already exists in the catalog. If your
   episode needs a topic that does not exist yet, add the topic first.
3. Keep titles short and avoid clickbait.

## Style notes

- No emojis in the catalog or in commit messages.
- No "feat:" or "fix:" prefixes. Write commit messages like a sentence.
- Frozen dataclasses only. If you need mutability, write a builder.
<!-- rev 1 -->
<!-- rev 5 -->
<!-- rev 9 -->
<!-- rev 13 -->
<!-- rev 17 -->
<!-- rev 21 -->
<!-- rev 25 -->
<!-- rev 29 -->
<!-- rev 33 -->
<!-- rev 37 -->
<!-- rev 41 -->
<!-- rev 45 -->
<!-- rev 49 -->
<!-- rev 53 -->
