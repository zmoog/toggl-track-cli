import datetime
import io

import click

from .toggl import TimeEntries
from .result import TimeEntriesListResult



@click.group()
@click.version_option()
def cli():
    "CLI tool and Python library to access Toggl Track https://toggl.com/track/"


@cli.group()
def entries():
    "entries command description"
    pass


@entries.command(name="list")
@click.option("--start-date", type=click.DateTime(), default=(datetime.datetime.now() - datetime.timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%S"))
@click.option("--end-date", type=click.DateTime(), default=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
def list_entries(start_date: datetime, end_date: datetime):
    """entries list command description"""

    client = TimeEntries.from_environment()

    click.echo(TimeEntriesListResult(
        client.list(start_date, end_date))
    )
