import datetime as dt
from typing import List

import click

from .toggl import TimeEntries
from .result import TimeEntriesListResult, TimeEntriesGroupByResult, GroupByCriterion, render


# default reference date for all date options
now = dt.datetime.now()

def as_str(reference_date: dt.datetime = now) -> str:
    """Formats a `reference_date` into a string.
    
    Helper function to be used as a default value for click options.

    :param reference_date: a datetime object"""
    return reference_date.strftime("%Y-%m-%dT%H:%M:%S")


@click.group()
@click.version_option()
@click.option(
    "--format",
    type=click.Choice(['json', 'ndjson', 'text'],
    case_sensitive=False),
    default="text",
)
@click.option(
    "--json-root",
    default=None,
)
@click.pass_context
def cli(ctx: click.Context, format: str, json_root: str):
    "CLI tool and Python library to access Toggl Track https://toggl.com/track/"
    ctx.ensure_object(dict)
    ctx.obj['format'] = format
    ctx.obj['json_root'] = json_root

@cli.group()
@click.option(
    '--description',
    '-d',
    type=click.STRING,
    multiple=False)
@click.option(
    '--project-id',
    '-p',
    type=click.INT,
    multiple=True)
@click.pass_context
def entries(ctx: click.Context, description: List[str], project_id: List[int]):
    "Time entries commands"
    ctx.ensure_object(dict)
    ctx.obj['description'] = description
    ctx.obj['project_id'] = project_id


@entries.command(name="list")
@click.option(
    "--start-date",
    type=click.DateTime(),
    default=as_str(now - dt.timedelta(hours=24)),
    help="Start date (default: 24 hours ago)"
)
@click.option(
    "--end-date",
    type=click.DateTime(),
    default=as_str(now)
)
@click.pass_context
def list_entries(ctx: click.Context, start_date: dt.datetime, end_date: dt.datetime):
    """Returns a list of the latest time entries (default: last 24 hours)"""

    client = TimeEntries.from_environment()

    click.echo(
        render(
            TimeEntriesListResult(
                client.list(start_date, end_date, project_ids=ctx.obj['project_id'], description=ctx.obj['description'])
            ),
            format=ctx.obj['format'],
            json_root=ctx.obj['json_root'],
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
    default=as_str(now - dt.timedelta(hours=24)),
    help="Start date (default: 24 hours ago)"
)
@click.option(
    "--end-date",
    type=click.DateTime(),
    default=as_str(now)
)
@click.pass_context
def group_by_entries(ctx: click.Context, start_date: dt.datetime, end_date: dt.datetime, field: str = "tags"):
    """Returns a list of time entries grouped by a field"""

    client = TimeEntries.from_environment()

    click.echo(
        render(
            TimeEntriesGroupByResult(
                client.list(start_date, end_date, project_ids=ctx.obj['project_id'], description=ctx.obj['description']),
                key_func=GroupByCriterion(field)
            ),
            format=ctx.obj['format'],
            json_root=ctx.obj['json_root'],
        ),
        nl=True,  # add a newline at the end of the output
    )
