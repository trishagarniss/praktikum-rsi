from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.backend.database.connection import get_session
from src.backend.dto.user_dto import UserInput, UserUpdate, UserResponse
from src.backend.controllers import user_controller

router = APIRouter(prefix="/users", tags=["Users"])

# 1. CREATE (POST)
@router.post("/", status_code=201, response_model=UserResponse)
def create_user_route(user: UserInput, db: Session = Depends(get_session)):
    return user_controller.create_user_controller(user=user, db=db)

# 2. READ ALL (GET)
@router.get("/", response_model=list[UserResponse])
def get_all_users_route(db: Session = Depends(get_session)):
    return user_controller.get_all_user_controller(db=db)

# 3. READ BY ID (GET)
@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id_route(user_id: int, db: Session = Depends(get_session)):
    return user_controller.get_user_by_id_controller(user_id=user_id, db=db)

# 4. UPDATE (PUT)
@router.put("/{user_id}", response_model=UserResponse)
def update_user_route(user_id: int, data: UserUpdate, db: Session = Depends(get_session)):
    return user_controller.update_user_controller(user_id=user_id, data=data, db=db)

# 5. DELETE (DELETE)
@router.delete("/{user_id}")
def delete_user_route(user_id: int, db: Session = Depends(get_session)):
    return user_controller.delete_user_controller(user_id=user_id, db=db)
