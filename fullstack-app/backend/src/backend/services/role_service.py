from sqlmodel import Session, select
from src.backend.repositories import role_repo # Pastikan path import ini benar
from src.backend.database.schema.models import Role
from src.backend.dto.role_dto import RoleCreate
from fastapi import HTTPException

# 1. CREATE
def add_new_role(db: Session, role_data: RoleCreate):
    # Validasi: Nama gak boleh kosong atau cuma spasi
    clean_name = role_data.name.strip()
    if not clean_name:
        raise HTTPException(status_code=400, detail="Nama role gak boleh kosong!")
    
    # Cek apakah nama role sudah ada di DB
    existing_role = db.exec(select(Role).where(Role.name == clean_name)).first()
    if existing_role:
        raise HTTPException(status_code=400, detail=f"Role '{clean_name}' sudah ada!")

    role_data.name = clean_name
    return role_repo.create_role(db, role_data)

# 2. READ ALL
def get_all_roles(db: Session):
    return role_repo.get_roles(db)

# 3. READ BY ID
def get_role(db: Session, role_id: int):
    role = role_repo.get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail=f"Role dengan ID {role_id} tidak ditemukan!")
    return role

# 4. UPDATE
def modify_role(db: Session, role_id: int, role_data: RoleCreate):
    clean_name = role_data.name.strip()
    if not clean_name:
        raise HTTPException(status_code=400, detail="Nama role gak boleh kosong!")
    
    role_data.name = clean_name
    updated_role = role_repo.update_role(db, role_id, role_data)
    if not updated_role:
        raise HTTPException(status_code=404, detail=f"Role dengan ID {role_id} tidak ditemukan!")
    return updated_role

# 5. DELETE
def remove_role(db: Session, role_id: int):
    success = role_repo.delete_role(db, role_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Role dengan ID {role_id} tidak ditemukan!")
    return {"message": f"Role dengan ID {role_id} berhasil dihapus"}