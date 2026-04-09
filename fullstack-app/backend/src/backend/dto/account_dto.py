from pydantic import BaseModel,EmailStr

class AccountCreate(BaseModel):
    user_id: int
    role_id: int
    email : EmailStr
    username : str
    password : str

class AccountResponse(BaseModel):
    id : int