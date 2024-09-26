from datetime import datetime, time, timedelta
from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    userId: str
    name: str
    profile: str