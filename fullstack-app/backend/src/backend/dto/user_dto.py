from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    whatsapp: str

class UserInput(User):
    pass
    
class UserUpdate(User):
    pass

class RoleResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True