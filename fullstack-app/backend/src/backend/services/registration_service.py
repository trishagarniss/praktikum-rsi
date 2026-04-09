from sqlmodel import Session
from src.backend.repositories import registration_repo
from src.backend.dto.registration_dto import RegistrationCreate
from fastapi import HTTPException

# 1. CREATE
def add_new_registration(db: Session, registration_data: RegistrationCreate):
    if not registration_data.user_id:
        raise HTTPException(status_code=400, detail="User ID is required")
    if not registration_data.event_id:
        raise HTTPException(status_code=400, detail="Event ID is required")
    return registration_repo.create_registration(db, registration_data)

# 2. READ ALL
def get_all_registrations(db: Session):
    return registration_repo.get_registrations(db)

# 3. READ BY ID
def get_registration(db: Session, registration_id: int):
    registration = registration_repo.get_registration_by_id(db, registration_id)
    if not registration:
        raise HTTPException(status_code=404, detail=f"Registration with ID {registration_id} not found!")
    return registration

# 4. UPDATE
def modify_registration(db: Session, registration_id: int, registration_data: RegistrationCreate):
    if not registration_data.user_id:
        raise HTTPException(status_code=400, detail="User ID is required")
    if not registration_data.event_id:
        raise HTTPException(status_code=400, detail="Event ID is required")
    
    updated_registration = registration_repo.update_registration(db, registration_id, registration_data)
    if not updated_registration:
        raise HTTPException(status_code=404, detail=f"Registration with ID {registration_id} not found!")
    return updated_registration

# 5. DELETE
def remove_registration(db: Session, registration_id: int):
    success = registration_repo.delete_registration(db, registration_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Registration with ID {registration_id} not found!")
    return {"message": f"Registration with ID {registration_id} successfully deleted"}