from sqlmodel import Session, select
from src.backend.database.schema.models import Registration
from src.backend.dto.registration_dto import RegistrationCreate, RegistrationResponse

# 1. CREATE (Buat Registration Baru)
def create_registration(db: Session, registration_create: RegistrationCreate):
    new_registration = Registration(user_id=registration_create.user_id, event_id=registration_create.event_id)
    db.add(new_registration)
    db.commit()
    db.refresh(new_registration)
    return new_registration

# 2. READ (Dapatkan Semua Registration)
def get_registrations(db: Session):
    return db.exec(select(Registration)).all()

# 3. READ BY ID (Dapatkan Registration Berdasarkan ID)
def get_registration_by_id(db: Session, registration_id: int):
    return db.get(Registration, registration_id)

# 4. UPDATE (Ubah Data Registration)
def update_registration(db:Session, registration_id: int, registration_data: RegistrationCreate):
    db_registration = db.get(Registration, registration_id)
    if db_registration:
        db.registration_user_id = registration_data.user_id
        db.registration_event_id = registration_data.event_id
        db.add(db_registration)
        db.commit()
        db.refresh(db_registration)
        return db_registration
    return None

# 5. DELETE (Hapus Data Registration)
def delete_registration(db: Session, registration_id: int):
    db_registration = db.get(Registration, registration_id)
    if db_registration:
        db.delete(db_registration)
        db.commit()
        return True
    return False