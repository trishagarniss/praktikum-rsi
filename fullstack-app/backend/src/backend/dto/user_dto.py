from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    whatsapp: str
    created_at: str
    updated_at: str

class UserInput(BaseModel):
    first_name: str
    last_name: str
    whatsapp: str
    
class UserUpdate(BaseModel):
    id: int
    first_name: str
    last_name: str
    whatsapp: str