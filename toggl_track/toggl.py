import os
import urllib
from datetime import datetime
from typing import Optional, Iterator, List

import requests
from pydantic import BaseModel, parse_raw_as


class TimeEntry(BaseModel):
    """TimeEntry model."""
    id: int
    workspace_id: int
    user_id: int
    project_id: int
    task_id: Optional[int]
    billable: bool
    at: datetime
    description: str
    start: datetime
    stop: Optional[datetime]
    duration: int
    tags: Optional[List[str]]

    @property
    def initiative(self) -> str:
        """Returns the initiative part of the description."""
        return self.description.split(":")[0]

class TimeEntries(object):
    """TimeEntries API client."""

    def __init__(self, api_token: str) -> None:
        self.api_token = api_token

    @classmethod
    def from_environment(cls) -> "TimeEntries":
        """Creates a new `TimeEntries` instance from the `TOGGL_API_TOKEN` environment variable."""
        if "TOGGL_API_TOKEN" not in os.environ:
            raise Exception(
                "TOGGL_API_TOKEN environment variable not found. "
                "Please set it to your Toggl Track API token."
            )
        return cls(api_token=os.environ["TOGGL_API_TOKEN"])

    def list(self, start_date: datetime, end_date: datetime, description: str = None, project_ids: List[int] = []) -> Iterator[TimeEntry]:
        """Fetches the time entries between `start_date` and `end_date` dates.
        
        Time Entries API v9
        https://developers.track.toggl.com/docs/api/time_entries
        """
        params = dict(
            start_date=start_date.isoformat() + "Z",
            end_date=end_date.isoformat() + "Z",
        )

        url = (
            "https://api.track.toggl.com/api/v9/me/time_entries?"
            + urllib.parse.urlencode(params)
        )

        resp = requests.get(url, auth=(self.api_token, "api_token"))
        if resp.status_code != 200:
            raise Exception(resp.text)

        # it looks like the API doesn't support filtering, so I suppose
        # we have to do it ourselves
        entries = parse_raw_as(List[TimeEntry], resp.text)

        if description:
            entries = filter(lambda entry: description in entry.initiative, entries)

        if project_ids:
            entries = filter(lambda entry: entry.project_id in project_ids, entries)
        
        return entries
