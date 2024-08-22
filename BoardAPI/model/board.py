from datetime import datetime, time, timedelta
from pydantic import BaseModel, Field

class Board(BaseModel):
    no: int
    title: str
    writer: str
    content: str
    regDate: datetime
    updDate: datetime
