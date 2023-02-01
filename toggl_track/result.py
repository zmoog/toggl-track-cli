import io
from itertools import groupby
from typing import Any, List

from humanize import naturaldelta
from rich import box
from rich.console import Console
from rich.table import Table

from .toggl import TimeEntry


class TimeEntriesListResult(object):
    """Turns a list of TimeEntry objects into a rich table"""

    def __init__(self, entries: List[TimeEntry]) -> None:
        self.entries = entries

    def __str__(self) -> str:
        """Returns a rich table as a string."""
        
        if not self.entries:
            return "No time entries found."

        table = Table(title="Time Entries", box=box.SIMPLE)
        table.add_column("At")
        table.add_column("Description")
        table.add_column("Start")
        table.add_column("Stop")
        table.add_column("Duration")
        table.add_column("Tags")

        for e in self.entries:
            table.add_row(
                e.at.strftime("%Y-%m-%d"),
                e.description,
                e.start.strftime("%I:%M %p"),
                "" if not e.stop else e.stop.strftime("%I:%M %p"),
                "" if e.duration < 0 else naturaldelta(e.duration),
                "" if not e.tags else "".join(e.tags),
            )

        # turn table into a string using the Console
        console = Console(file=io.StringIO())
        console.print(table)

        return console.file.getvalue()


class GroupByCriterion(object):
    """MISSING DOCSTRING"""

    def __init__(self, name: str) -> None:
        self.name = name

    def __call__(self, time_entry: TimeEntry) -> Any:
        v = getattr(time_entry, self.name)
        if isinstance(v, List):
            return "".join(v)
        return v

class TimeEntriesGroupByResult(object):
    """MISSING DOCSTRING"""

    def __init__(self, entries: List[TimeEntry], key_func: GroupByCriterion) -> None:
        self.key_func = key_func

        # group entries by key_func
        grouped_entries = groupby(
            sorted(  # sort before grouping
                entries,
                key=key_func,
            ),
            key=key_func)

        # sum up the durations of each group
        self.entries = [(
            k,
            sum([e.duration for e in g if e.duration > 0])
        ) for k, g in grouped_entries]

        # sort by duration
        self.entries = sorted(self.entries, key=lambda x: x[1], reverse=True)

    def __str__(self) -> str:
        """Returns a rich table as a string."""
        
        if not self.entries:
            return "No time entries found."

        table = Table(title="Time Entries", box=box.SIMPLE)
        table.add_column(self.key_func.name)
        table.add_column("Duration")

        for k, g in self.entries:
            # total_duration = sum([e.duration for e in g if e.duration > 0])
            table.add_row(
                k,
                "-" if g < 0 else naturaldelta(g),
            )

        # turn table into a string using the Console
        console = Console(file=io.StringIO())
        console.print(table)

        return console.file.getvalue()
