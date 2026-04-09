from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    whatsapp: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
class UserInput(BaseModel):
    first_name: str
    last_name: str
    whatsapp: str
    
class UserUpdate(BaseModel):
    id: int
    first_name: str
    last_name: str
    whatsapp: str