"""Print every research topic in the catalog as a tiny report."""
from tvbridge.catalog import TOPICS


def main() -> None:
    for slug, topic in sorted(TOPICS.items()):
        print(f"[{topic.channel:>9}] {slug:<22} d{topic.difficulty}  {topic.title}")


if __name__ == "__main__":
    main()
