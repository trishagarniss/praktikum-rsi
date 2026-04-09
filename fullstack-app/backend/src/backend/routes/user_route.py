from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.backend.database.connection import get_session
from src.backend.dto.user_dto import User,UserInput,UserUpdate
from src.backend.controllers import user_controller
from typing import List, Union


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", status_code=201)
def create_user_route(user: UserInput):
    return user_controller.create_user_controller(user)

# 2. READ ALL (GET)
@router.get("/", response_model=Union[List[User], User])
def get_all_roles_route():
    return user_controller.get_all_user_controller()

# 3. READ BY ID (GET)
@router.get("/{user_id}", response_model=Union[List[User], User])
def get_user_by_id_route(user_id: int):
    return user_controller.get_user_by_id_controller(user_id=user_id)

# 4. UPDATE (PUT)
@router.put("/{user_id}")
def update_role_route(user_id : int, data : UserInput):
    data_baru = UserUpdate(
        id=user_id,
        first_name= data.first_name,
        last_name= data.last_name,
        whatsapp= data.whatsapp
    )
    return user_controller.update_user_controller(data=data_baru)

# 5. DELETE (DELETE)
@router.delete("/{user_id}")
def delete_role_route(user_id: int):
    return user_controller.delete_user_controller(id=user_id)