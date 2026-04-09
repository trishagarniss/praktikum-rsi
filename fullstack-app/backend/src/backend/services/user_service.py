from fastapi import HTTPException
from sqlmodel import Session
from src.backend.dto.user_dto import UserInput, UserUpdate
from src.backend.repositories import user_repo as ur

# 1. CREATE
def tambah_user(db: Session, data_user: UserInput):
    if not data_user.first_name.strip():
        raise HTTPException(status_code=400, detail="First name tidak boleh kosong")
    
    return ur.create_user(db, data_user)

# 2. READ ALL
def tampilkan_user(db: Session):
    return ur.get_users(db)

# 3. READ BY ID
def tampilkan_user_by_id(db: Session, user_id: int):
    user = ur.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User dengan id {user_id} tidak ditemukan")
    return user

# 4. UPDATE
def edit_user(db: Session, user_id: int, data_user: UserUpdate):
    user = ur.update_user(db, user_id, data_user)
    if not user:
        raise HTTPException(status_code=404, detail=f"User dengan id {user_id} tidak ditemukan")
    return user
    
# 5. DELETE
def hapus_user(db: Session, user_id: int):
    success = ur.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"User dengan id {user_id} tidak ditemukan")
    return {"message": f"User dengan id {user_id} berhasil dihapus"}