import datetime
import io
import io

import click
from humanize import naturaldelta
from rich import box
from rich.console import Console
from rich.table import Table

from .toggl import TimeEntries



@click.group()
@click.version_option()
def cli():
    "CLI tool and Python library to access Toggl Track https://toggl.com/track/"


@cli.command(name="command")
@click.argument(
    "example"
)
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def first_command(example, option):
    "Command description goes here"
    click.echo("Here is some output")


@cli.group()
def entries():
    "entries command description"
    pass


@entries.command(name="list")
@click.option("--start-date", type=click.DateTime(), default=(datetime.datetime.now() - datetime.timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%S"))
@click.option("--end-date", type=click.DateTime(), default=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
def list_entries(start_date: datetime, end_date: datetime):
    """entries list command description"""

    time_entries = TimeEntries.from_environment()
    entries = time_entries.list(start_date, end_date)

    # print(entries)

    table = Table(title="Time Entries", box=box.SIMPLE)
    table.add_column("At")
    table.add_column("Description")
    table.add_column("Start")
    table.add_column("Stop")
    table.add_column("Duration")
    table.add_column("Tags")

    for e in entries:
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

    click.echo(console.file.getvalue())