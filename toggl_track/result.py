import io
from typing import Optional, List

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
                # "",
                # "2023-01-25",
                # "community: https://github.com/elastic/beats/issues/34330",
                # "11:04 PM",
                # "11:27 PM",
                # "0:22:59",
                # "type:support"
            )

        # turn table into a string using the Console
        console = Console(file=io.StringIO())
        console.print(table)

        # click.echo(console.file.getvalue())
        return console.file.getvalue()
