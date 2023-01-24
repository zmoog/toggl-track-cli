# toggl-track

[![PyPI](https://img.shields.io/pypi/v/toggl-track.svg)](https://pypi.org/project/toggl-track/)
[![Changelog](https://img.shields.io/github/v/release/zmoog/toggl-track?include_prereleases&label=changelog)](https://github.com/zmoog/toggl-track/releases)
[![Tests](https://github.com/zmoog/toggl-track/workflows/Test/badge.svg)](https://github.com/zmoog/toggl-track/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/zmoog/toggl-track/blob/master/LICENSE)

CLI tool and Python library to access Toggl Track https://toggl.com/track/

## Installation

Install this tool using `pip`:

    pip install toggl-track

## Usage

For help, run:

    toggl-track --help

You can also use:

    python -m toggl_track --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd toggl-track
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
