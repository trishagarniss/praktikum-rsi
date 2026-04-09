from sqlmodel import Session
from src.backend.services import user_service
from src.backend.dto.user_dto import User,UserInput,UserUpdate

def create_user_controller(user : UserInput):
    return user_service.tambah_user(data_user = user)

# 2. READ ALL
def get_all_user_controller():
    return user_service.tampilkan_user()

# 3. READ BY ID
def get_user_by_id_controller(user_id: int):
    return user_service.tampilkan_user(id = user_id)

# 4. UPDATE
def update_user_controller(data : UserUpdate):
    return user_service.edit_user(data_user= data)

# 5. DELETE
def delete_user_controller(id: int):
    return user_service.hapus_user(id_input=id)