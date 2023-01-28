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

For listing the time entries in the last 24 hours, run:

    $ tgl entries list
                                                                    Time Entries                                                                     
                                                                                                                                                     
      At           Description                                                                  Start      Stop       Duration         Tags          
     ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
      2023-01-28   toggl-track: list time entries                                               04:33 AM                                         
      2023-01-27   ESF: telemetry                                                               05:23 PM   07:19 PM   an hour          type:goal     
      2023-01-27   ESF: telemetry                                                               03:28 PM   05:00 PM   an hour          type:goal     
      2023-01-27   Community: Fix parsing error client port is blank and adjust for timeStamp   03:13 PM   03:28 PM   15 minutes       type:support  
      2023-01-27   Community: Azure Signin Module authentication_processing_details Issue       02:47 PM   03:13 PM   25 minutes       type:support  
      2023-01-27   sync                                                                         02:31 PM   02:47 PM   16 minutes       type:sync     
      2023-01-27   🍜 Lunch                                                                     01:11 PM   02:31 PM   an hour                    
      2023-01-27   Community: Fix parsing error client port is blank and adjust for timeStamp   12:19 PM   12:29 PM   10 minutes       type:support  
      2023-01-27   Community: Fix parsing error client port is blank and adjust for timeStamp   11:54 AM   12:06 PM   11 minutes       type:support  
      2023-01-27   Community: Azure Signin Module authentication_processing_details Issue       09:30 AM   11:54 AM   2 hours          type:support  
      2023-01-27   sync                                                                         08:34 AM   09:30 AM   56 minutes       type:sync     
      2023-01-27   toggl-track: list time entries                                               07:04 AM   08:34 AM   an hour                    

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
