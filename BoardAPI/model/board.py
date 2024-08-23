from datetime import datetime, time, timedelta
from pydantic import BaseModel, Field
from typing import Optional

class Board(BaseModel):
    no: Optional[int] = 0
    title: str
    writer: str
    content: str
    regDate: Optional[datetime] = None
    updDate: Optional[datetime] = None