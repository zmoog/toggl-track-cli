from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class TimeEntry(BaseModel):
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
