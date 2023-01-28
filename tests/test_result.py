from datetime import datetime

from toggl_track.result import TimeEntriesListResult
from toggl_track.toggl import TimeEntry


def test_empty_timeentrieslistresult_as_str():
    entries = []
    result = TimeEntriesListResult(entries)

    assert str(result) == "No time entries found."


def test_empty_timeentrieslistresult_as_str():
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

    assert str(result) == """                                 Time Entries                                 
                                                                              
  At           Description   Start      Stop       Duration     Tags          
 ──────────────────────────────────────────────────────────────────────────── 
  2021-01-25   community:    11:04 PM   11:27 PM   22 minutes   type:support  
                                                                              
"""
