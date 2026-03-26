"""Print every broadcast episode in the catalog."""
from tvbridge.catalog import EPISODES


def main() -> None:
    for number in sorted(EPISODES):
        ep = EPISODES[number]
        topics = ", ".join(ep.topic_slugs)
        print(f"{ep.code}  {ep.air_date}  [{ep.channel}] {ep.title}  ({topics})")


if __name__ == "__main__":
    main()
