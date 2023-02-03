import datetime
from datetime import timedelta

import click

from .toggl import TimeEntries
from .result import TimeEntriesListResult, TimeEntriesGroupByResult, GroupByCriterion


# default reference date for all date options
now = datetime.datetime.now()

def as_str(reference_date: datetime = now) -> str:
    """Formats a `reference_date` into a string.
    
    Helper function to be used as a default value for click options.

    :param reference_date: a datetime object"""
    return reference_date.strftime("%Y-%m-%dT%H:%M:%S")


@click.group()
@click.version_option()
def cli():
    "CLI tool and Python library to access Toggl Track https://toggl.com/track/"


@cli.group()
def entries():
    "Time entries commands"
    pass


@entries.command(name="list")
@click.option(
    "--start-date",
    type=click.DateTime(),
    default=as_str(now - timedelta(hours=24)),
    help="Start date (default: 24 hours ago)"
)
@click.option(
    "--end-date",
    type=click.DateTime(),
    default=as_str(now)
)
def list_entries(start_date: datetime, end_date: datetime):
    """Returns a list of the latest time entries (default: last 24 hours)"""

    client = TimeEntries.from_environment()

    click.echo(
        TimeEntriesListResult(
            client.list(start_date, end_date)
        )
    )


@entries.command(name="group-by")
@click.option(
    "--field",
    required=True,
)
@click.option(
    "--start-date",
    type=click.DateTime(),
    default=as_str(now - timedelta(hours=24)),
    help="Start date (default: 24 hours ago)"
)
@click.option(
    "--end-date",
    type=click.DateTime(),
    default=as_str(now)
)
def group_by_entries(start_date: datetime, end_date: datetime, field: str = "tags"):
    """Returns a list of time entries grouped by a field"""

    client = TimeEntries.from_environment()

    click.echo(
        TimeEntriesGroupByResult(
            client.list(start_date, end_date),
            key_func=GroupByCriterion(field)
        )
    )
