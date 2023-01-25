import io

import click
from rich import box
from rich.console import Console
from rich.table import Table

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
def list_entries():
    """entries list command description"""
    table = Table(title="Time Entries", box=box.SIMPLE)
    table.add_column("Date")
    table.add_column("Description")
    table.add_column("Start")
    table.add_column("Stop")
    table.add_column("Duration")
    table.add_column("Tags")

    table.add_row(
        "2023-01-25",
        "community: https://github.com/elastic/beats/issues/34330",
        "11:04 PM",
        "11:27 PM",
        "0:22:59",
        "type:support"
    )

    # turn table into a string using the Console
    console = Console(file=io.StringIO())
    console.print(table)

    click.echo(console.file.getvalue())