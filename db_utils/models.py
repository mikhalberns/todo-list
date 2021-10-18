import datetime
from typing import Optional, List

from pydantic import BaseModel


class Item(BaseModel):
    user: str
    task: str
    created_date: datetime.datetime = datetime.datetime.today()
    due_date: datetime.datetime = None
    tags: Optional[List[str]]
