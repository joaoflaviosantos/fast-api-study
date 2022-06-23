from datetime import datetime
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Track(BaseModel):
    id: Optional[int]
    title: str
    artist: str
    duration: float
    last_play: datetime
