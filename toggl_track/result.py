import io
import json
from itertools import groupby
from typing import Any, Iterator, List

from pydantic.json import pydantic_encoder
from rich import box
from rich.console import Console
from rich.table import Table

from .toggl import TimeEntry


class TimeEntriesListResult(object):
    """Turns a TimeEntry iterator into a rich table"""

    def __init__(self, entries: Iterator[TimeEntry]) -> None:
        self.entries = list(entries)  # we iterate over the entries twice

    def __str__(self) -> str:
        """Returns a rich table as a string."""
        
        if not self.entries:
            return "No time entries found."

        # calculate total duration of all entries for the footer
        total = sum(e.duration for e in self.entries if e.duration > 0)

        table = Table(title="Time Entries", box=box.SIMPLE)
        table.add_column("At")
        table.add_column("Description")
        table.add_column("Start")
        table.add_column("Stop", "Total")
        table.add_column("Duration", format_duration(total))
        table.add_column("Tags")

        for e in self.entries:
            table.add_row(
                e.at.strftime("%Y-%m-%d"),
                # str(e.project_id),
                e.description,
                e.start.strftime("%I:%M %p"),
                "" if not e.stop else e.stop.strftime("%I:%M %p"),
                format_duration(e.duration),
                "" if not e.tags else "".join(e.tags),
            )

        # make footer with total duration visible
        table.show_footer = True

        # turn table into a string using the Console
        console = Console(file=io.StringIO())
        console.print(table)

        return console.file.getvalue()

    def json(self, root: str = None) -> str:
        """Returns a JSON string."""
        if root:
            result = {root: self.entries}
        else:
            result = self.entries
        
        return json.dumps(result, default=pydantic_encoder)
        
    def ndjson(self) -> str:
        """Returns a newline-delimited JSON string."""
        return "\n".join([e.json() for e in self.entries])


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
    """Turns a TimeEntry iterator into a rich table grouped by a criterion."""

    def __init__(self, entries: Iterator[TimeEntry], key_func: GroupByCriterion) -> None:
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

        # calculate total duration of all entries for the footer
        total = sum([e[1] for e in self.entries if e[1] > 0])

        table = Table(title="Time Entries", box=box.SIMPLE)
        table.add_column(self.key_func.name, "Total")
        table.add_column("Duration", str(format_duration(total)))

        for k, g in self.entries:
            table.add_row(
                k,
                format_duration(g),
            )

        # make footer with total duration visible
        table.show_footer = True

        # turn table into a string using the Console
        console = Console(file=io.StringIO())
        console.print(table)

        return console.file.getvalue()

    def json(self, root: str = None) -> str:
        """Returns a JSON string."""
        if root:
            result = {root: self.entries}
        else:
            result = self.entries
        return json.dumps(result)

    def ndjson(self) -> str:
        """Returns a newline-delimited JSON string."""
        return "\n".join([json.dumps({"field": self.key_func.name, "name": k, "duration": v}) for k, v in self.entries])


def render(result: Any, format: str = "text", json_root: str = None) -> str:
    """Renders a result object as a string."""
    if format == "json":
        return result.json(root=json_root)
    if format == "ndjson":
        return result.ndjson()
    return str(result)


def format_duration(duration: int) -> str:
    """Formats a duration in seconds as a string in the format HH:MM"""

    if duration < 0:  # happens when a time entry is still running
        return "-"
    
    # credits: 'inspired' by timedelta.__str__
    mm, _ = divmod(duration, 60)
    hh, mm = divmod(mm, 60)
    s = "%d:%02d" % (hh, mm)
    
    return s
