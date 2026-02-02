"""TVBridge: VHS-style broadcast catalog for ZK and interop research."""
from tvbridge.__version__ import __version__
from tvbridge.core.episode import BroadcastEpisode
from tvbridge.core.topic import ResearchTopic
from tvbridge.core.schedule import WeeklySchedule

__all__ = [
    "__version__",
    "BroadcastEpisode",
    "ResearchTopic",
    "WeeklySchedule",
]
