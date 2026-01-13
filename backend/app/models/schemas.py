from pydantic import BaseModel
from datetime import datetime

class LogEntry(BaseModel):
    timestamp: datetime
    level: str
    service: str
    message: str


