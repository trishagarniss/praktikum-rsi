from sqlmodel import Session, select
from src.backend.dto.user_dto import User,UserInput,UserUpdate
from src.backend.database.schema.models import User as Us
from datetime import datetime


# 1. CREATE (Buat Role Baru)
def create_user(db: Session, data: User):
    x = Us(
        first_name=data.first_name,
        last_name=data.last_name,
        whatsapp=data.whatsapp
    )
    db.add(x)
    db.commit()
    db.refresh(x)
    return x

# 2. READ (Dapatkan Semua Role)
def get_users(db: Session):
    return db.exec(select(Us)).all()

# 3. READ BY ID (Dapatkan Role Berdasarkan ID)
def get_user_by_id(db: Session, user_id: int):
    return db.get(Us, user_id)

# 4. UPDATE (Ubah Data Role)
def update_user(db:Session, user_data: User, time: datetime):
    db_user = db.get(Us, user_data.id)
    if db_user:
        db_user.first_name = user_data.first_name
        db_user.last_name = user_data.last_name
        db_user.whatsapp = user_data.whatsapp
        db_user.updated_at = time
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

# 5. DELETE (Hapus Data Role)
def delete_user(db: Session, user_id: int):
    db_user = db.get(Us, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return db_user