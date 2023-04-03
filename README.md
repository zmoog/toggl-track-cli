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

    At           Description                                                                  Start      Stop       Duration   Tags
    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    2023-02-04   toggl-track: insights                                                        05:37 AM              -
    2023-02-03   Community: Allow parsing of IPv6 addresses in ingest pipeline                08:18 PM   10:09 PM   1:51       type:support
    2023-02-03   🍲 Dinner                                                                    07:19 PM   08:18 PM   0:58
    2023-02-03   sync                                                                         06:19 PM   06:55 PM   0:35       type:sync
    2023-02-03   🚌 Shuttling kids between home and whatever                                  04:46 PM   06:19 PM   1:33
    2023-02-03   App Service logs integration: troubleshootign lucianpy issues                04:40 PM   04:46 PM   0:06       type:goal
    2023-02-03   Community: Allow parsing of IPv6 addresses in ingest pipeline                04:21 PM   04:40 PM   0:18       type:support
    2023-02-03   Community: Fix parsing error client port is blank and adjust for timeStamp   03:15 PM   04:21 PM   1:05       type:support
    2023-02-03   Community: Azure Signin Module authentication_processing_details Issue       02:37 PM   03:15 PM   0:38       type:support
    2023-02-03   Rosanna                                                                      11:06 AM   02:37 PM   3:31
    2023-02-03   Community: Azure Signin Module authentication_processing_details Issue       09:25 AM   11:06 AM   1:41       type:support
    2023-02-03   sync                                                                         08:37 AM   09:25 AM   0:48       type:sync
    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                                                        Total      13:08

Now you can also filter time entries by project ID or description:

    $ tgl entries --project-id 178435728 list
                                                                Time Entries

    At           Description                                                                  Start      Stop       Duration   Tags
    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    2023-02-03   Community: Allow parsing of IPv6 addresses in ingest pipeline                08:18 PM   10:09 PM   1:51       type:support
    2023-02-03   sync                                                                         06:19 PM   06:55 PM   0:35       type:sync
    2023-02-03   App Service logs integration: troubleshootign lucianpy issues                04:40 PM   04:46 PM   0:06       type:goal
    2023-02-03   Community: Allow parsing of IPv6 addresses in ingest pipeline                04:21 PM   04:40 PM   0:18       type:support
    2023-02-03   Community: Fix parsing error client port is blank and adjust for timeStamp   03:15 PM   04:21 PM   1:05       type:support
    2023-02-03   Community: Azure Signin Module authentication_processing_details Issue       02:37 PM   03:15 PM   0:38       type:support
    2023-02-03   Community: Azure Signin Module authentication_processing_details Issue       09:25 AM   11:06 AM   1:41       type:support
    2023-02-03   sync                                                                         08:37 AM   09:25 AM   0:48       type:sync
    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                                                        Total      7:05

    $ tgl entries --description SDH list

                                Time Entries                                
                                                                                
    At           Description   Start      Stop       Duration   Tags          
    ────────────────────────────────────────────────────────────────────────── 
    2023-04-01   SDH 3256      05:56 AM   07:01 AM   1:04       type:support  
    2023-03-31   SDH 3256      03:01 PM   04:18 PM   1:17       type:support  
    2023-03-31   SDH 3247      09:45 AM   12:04 PM   2:18       type:support  
    2023-03-31   SDH 3253      08:49 AM   09:45 AM   0:56       type:support  
    2023-03-31   SDH 3237      07:22 AM   08:30 AM   1:08       type:support  
    2023-03-30   SDH 3229      01:16 PM   05:35 PM   4:18       type:support  
    2023-03-30   SDH 3229      09:36 AM   11:31 AM   1:55       type:support  
    2023-04-03   SDH 3140      08:11 AM   09:19 AM   1:07       type:support  
    2023-03-29   SDH 3149      01:36 PM   05:04 PM   3:27       type:support  
    2023-03-28   SDH 3237      05:04 PM   06:03 PM   0:58       type:support  
    2023-03-28   SDH 3237      02:40 PM   03:01 PM   0:20       type:support  
    2023-03-28   SDH 3237      01:43 PM   02:21 PM   0:38       type:support  
    2023-03-28   SDH 3237      10:31 AM   12:17 PM   1:46       type:support  
    2023-03-27   SDH 3069      08:50 PM   09:29 PM   0:39       type:support  
    2023-03-27   SDH 3069      05:51 PM   06:56 PM   1:05       type:support  
    2023-03-27   SDH 3069      04:59 PM   05:21 PM   0:21       type:support  
    2023-03-27   SDH 3069      01:11 PM   03:09 PM   1:57       type:support  
    ──────────────────────────────────────────────────────────────────────────
                                            Total      25:22

Supports JSON and NDJSON as alternative output format using the  `--format` option:

    # format result as a list of objects
    $ tgl --format ndjson entries --project-id 178435728 list

    [{"id": 2848841800, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-02-16T15:54:40+00:00", "description": "Observability Demo Day",  ... "stop": "2023-02-16T06:59:01+00:00", "duration": 314, "tags": ["type:goal"]}]

    # optionally, format result as a root element that contains the list of objects using the `--json-root` option
    $ tgl --format ndjson --json-root entries entries --project-id 178435728 list


    $ tgl --format ndjson entries --project-id 178435728 list

    {"id": 2832493940, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-02-06T10:31:24+00:00", "description": "ESF: send after input has output", "start": "2023-02-06T09:40:10+00:00", "stop": "2023-02-06T10:31:24+00:00", "duration": 3074, "tags": ["type:goal"]}
    {"id": 2832473617, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-02-06T09:34:53+00:00", "description": "Maurizio / Tom", "start": "2023-02-06T08:58:17+00:00", "stop": "2023-02-06T09:29:22+00:00", "duration": 1865, "tags": ["type:meeting"]}
    {"id": 2832337954, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-02-06T09:34:39+00:00", "description": "sync", "start": "2023-02-06T08:15:08+00:00", "stop": "2023-02-06T08:57:17+00:00", "duration": 2529, "tags": ["type:sync"]}

For grouping time entries by tags and sum up the totals, run:

    $ tgl entries --project-id 178435728 group-by --field tags --start-date 2023-02-01
        Time Entries

    tags           Duration
    ─────────────────────────
    type:support   7:13
    type:goal      5:10
    type:meeting   4:29
    type:sync      3:38
    type:hr        0:09
    ─────────────────────────
    Total          20:40

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

If you need to send other requests to Toggl API, you can capture responses using:

   pytest --record-mode=once
