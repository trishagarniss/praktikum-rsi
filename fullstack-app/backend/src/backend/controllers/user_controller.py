from sqlmodel import Session
from src.backend.services import user_service
from src.backend.dto.user_dto import UserInput, UserUpdate

# 1. CREATE
def create_user_controller(user: UserInput, db: Session):
    return user_service.tambah_user(db=db, data_user=user)

# 2. READ ALL
def get_all_user_controller(db: Session):
    return user_service.tampilkan_user(db=db)

# 3. READ BY ID
def get_user_by_id_controller(user_id: int, db: Session):
    return user_service.tampilkan_user_by_id(db=db, user_id=user_id)

# 4. UPDATE
def update_user_controller(user_id: int, data: UserUpdate, db: Session):
    return user_service.edit_user(db=db, user_id=user_id, data_user=data)

# 5. DELETE
def delete_user_controller(user_id: int, db: Session):
    return user_service.hapus_user(db=db, user_id=user_id)
