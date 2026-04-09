from sqlmodel import Session
from src.backend.services import user_service
from src.backend.dto.user_dto import User,UserInput,UserUpdate

def create_user_controller(db: Session, user : UserInput):
    return user_service.tambah_user(data_user = user, session = db)

# 2. READ ALL
def get_all_user_controller(db: Session):
    return user_service.tampilkan_user(session = db)

# 3. READ BY ID
def get_user_by_id_controller(db: Session, user_id: int):
    return user_service.tampilkan_user(session = db, id = user_id)

# 4. UPDATE
def update_user_controller(db: Session, data : UserUpdate):
    return user_service.edit_user(session = db, data_user= data)

# 5. DELETE
def delete_user_controller(db: Session, id: int):
    return user_service.hapus_user(session = db, id_input=id)