from sqlmodel import Session
from src.backend.services import registration_service
from src.backend.dto.registration_dto import RegistrationCreate

# 1. CREATE
def create_registration_controller(registration: RegistrationCreate, db: Session):
    return registration_service.add_new_registration(db, registration)

# 2. READ ALL
def get_all_registrations_controller(db: Session):
    return registration_service.get_all_registrations(db)

# 3. READ BY ID
def get_registration_by_id_controller(registration_id: int, db: Session):
    return registration_service.get_registration(db, registration_id)

# 4. UPDATE
def update_registration_controller(registration_id: int, registration: RegistrationCreate, db: Session):
    return registration_service.modify_registration(db, registration_id, registration)

# 5. DELETE
def delete_registration_controller(registration_id: int, db: Session):
    return registration_service.remove_registration(db, registration_id)