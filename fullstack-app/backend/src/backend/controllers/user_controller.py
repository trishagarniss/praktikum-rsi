from sqlmodel import Session
from src.backend.services import user_service
from src.backend.dto.user_dto import UserInput,UserUpdate


def create_user_controller(user : UserInput,db:Session):
    return user_service.tambah_user(data_user = user,db=db)

# 2. READ ALL
def get_all_user_controller(db:Session):
    return user_service.tampilkan_user(db=db)

# 3. READ BY ID
def get_user_by_id_controller(user_id: int,db:Session):
    return user_service.tampilkan_user(id = user_id,db=db)

# 4. UPDATE
def update_user_controller(data : UserUpdate,db:Session):
    return user_service.edit_user(data_user= data,db=db)

# 5. DELETE
def delete_user_controller(id: int,db:Session):
    return user_service.hapus_user(id_input=id,db=db)