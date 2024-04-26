from datetime import datetime

from toggl_track.result import TimeEntriesListResult
from toggl_track.toggl import TimeEntry


def test_empty_timeentrieslistresult_as_str():
    entries = []
    result = TimeEntriesListResult(entries)

    assert str(result) == "No time entries found."


def test_timeentrieslistresult_as_str(save_to_tmp):
    entries = [TimeEntry(
        id=1,
        workspace_id=1,
        user_id=1,
        project_id=1,
        task_id=None,
        billable=False,
        at=datetime(2021, 1, 25, 0, 0),
        description="community:",
        start=datetime(2021, 1, 25, 23, 4),
        stop=datetime(2021, 1, 25, 23, 27),
        duration=1379,
        tags=["type:support"]
    )]
    result = TimeEntriesListResult(entries)

    save_to_tmp(result, "test_empty_timeentrieslistresult_as_str")

    assert str(result) == """                                Time Entries                                
                                                                            
  At           Description   Start      Stop       Duration   Tags          
 ────────────────────────────────────────────────────────────────────────── 
  2021-01-25   community:    11:04 PM   11:27 PM   0:22       type:support  
 ────────────────────────────────────────────────────────────────────────── 
                                        Total      0:22                     
                                                                            
"""


def test_timeentrieslistresult_as_json(save_to_tmp):
    entries = [TimeEntry(
        id=1,
        workspace_id=1,
        user_id=1,
        project_id=1,
        task_id=None,
        billable=False,
        at=datetime(2021, 1, 25, 0, 0),
        description="community:",
        start=datetime(2021, 1, 25, 23, 4),
        stop=datetime(2021, 1, 25, 23, 27),
        duration=1379,
        tags=["type:support"]
    )]
    result = TimeEntriesListResult(entries)

    json_result = result.json()
    save_to_tmp(json_result, "test_empty_timeentrieslistresult_as_json")

    assert json_result == """[{"id": 1, "workspace_id": 1, "user_id": 1, "project_id": 1, "task_id": null, "billable": false, "at": "2021-01-25T00:00:00", "description": "community:", "start": "2021-01-25T23:04:00", "stop": "2021-01-25T23:27:00", "duration": 1379, "tags": ["type:support"]}]"""


def test_timeentrieslistresult_as_json_with_root(save_to_tmp):
    entries = [TimeEntry(
        id=1,
        workspace_id=1,
        user_id=1,
        project_id=1,
        task_id=None,
        billable=False,
        at=datetime(2021, 1, 25, 0, 0),
        description="community:",
        start=datetime(2021, 1, 25, 23, 4),
        stop=datetime(2021, 1, 25, 23, 27),
        duration=1379,
        tags=["type:support"]
    )]
    result = TimeEntriesListResult(entries)

    json_result = result.json(root="time_entries")
    save_to_tmp(json_result, "test_empty_timeentrieslistresult_as_json_with_root")

    assert json_result == """{"time_entries": [{"id": 1, "workspace_id": 1, "user_id": 1, "project_id": 1, "task_id": null, "billable": false, "at": "2021-01-25T00:00:00", "description": "community:", "start": "2021-01-25T23:04:00", "stop": "2021-01-25T23:27:00", "duration": 1379, "tags": ["type:support"]}]}"""
