from fastapi import HTTPException
from sqlmodel import Session
from src.backend.dto.event_dto import EventCreate, EventUpdate
from src.backend.repositories import event_repo

# 1. CREATE
def add_new_event(db: Session, event_data: EventCreate):
    if not event_data.name.strip():
        raise HTTPException(status_code=400, detail="Nama event tidak boleh kosong")
    
    if event_data.quota <= 0:
        raise HTTPException(status_code=400, detail="Kuota event harus lebih dari 0")
        
    if event_data.started_at >= event_data.ended_at:
        raise HTTPException(status_code=400, detail="Waktu mulai harus lebih awal dari waktu selesai")

    return event_repo.create_event(db, event_data)

# 2. READ ALL
def get_all_events(db: Session):
    return event_repo.get_events(db)

# 3. READ BY ID
def get_event(db: Session, event_id: int):
    event = event_repo.get_event_by_id(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail=f"Event dengan ID {event_id} tidak ditemukan")
    return event

# 4. UPDATE
def modify_event(db: Session, event_id: int, event_data: EventUpdate):
    # Validasi lagi saat update
    if event_data.quota <= 0:
        raise HTTPException(status_code=400, detail="Kuota event harus lebih dari 0")
        
    if event_data.started_at >= event_data.ended_at:
        raise HTTPException(status_code=400, detail="Waktu mulai harus lebih awal dari waktu selesai")

    event = event_repo.update_event(db, event_id, event_data)
    if not event:
        raise HTTPException(status_code=404, detail=f"Event dengan ID {event_id} tidak ditemukan")
    return event

# 5. DELETE
def remove_event(db: Session, event_id: int):
    success = event_repo.delete_event(db, event_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Gagal menghapus. Event dengan ID {event_id} tidak ditemukan")
    
    return {"message": f"Event dengan ID {event_id} berhasil dihapus dari sistem"}