from sqlmodel import Session, select
from src.backend.database.schema.models import Role
from src.backend.dto.role_dto import RoleCreate

# 1. CREATE (Buat Role Baru)
def create_role(db: Session, role_create: RoleCreate):
    new_role = Role(name=role_create.name)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

# 2. READ (Dapatkan Semua Role)
def get_roles(db: Session):
    return db.exec(select(Role)).all()

# 3. READ BY ID (Dapatkan Role Berdasarkan ID)
def get_role_by_id(db: Session, role_id: int):
    return db.get(Role, role_id)

# 4. UPDATE (Ubah Data Role)
def update_role(db: Session, role_id: int, role_data: RoleCreate):
    db_role = db.get(Role, role_id)
    if db_role:
        db_role.name = role_data.name # Ubah ini
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
        return db_role
    return None

# 5. DELETE (Hapus Data Role)
def delete_role(db: Session, role_id: int):
    db_role = db.get(Role, role_id)
    if db_role:
        db.delete(db_role)
        db.commit()
        return True
    return False