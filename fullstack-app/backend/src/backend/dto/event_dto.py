from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventBase(BaseModel):
    name: str  # Menggantikan title
    description: str
    quota: Optional[int] = None
    started_at: datetime # Menggantikan date
    ended_at: datetime

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    name: Optional[str] = None
    description: Optional[str] = None
    quota: Optional[int] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None

class EventResponse(EventBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True