from fastapi import HTTPException
from sqlmodel import Session
from src.backend.repositories import event_repo
from src.backend.dto.event_dto import EventCreate, EventUpdate

def add_new_event(db: Session, event_data: EventCreate):
    # Ubah title menjadi name
    if not event_data.name.strip():
        raise HTTPException(status_code=400, detail="Nama event wajib diisi!")
    return event_repo.create_event(db, event_data)

def get_event_detail(db: Session, event_id: int):
    event = event_repo.get_event_by_id(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event tidak ditemukan")
    return event

def remove_event(db: Session, event_id: int):
    # Memanggil fungsi delete dari repository
    success = event_repo.delete_event(db, event_id)
    
    # Jika data tidak ada, kembalikan error 404
    if not success:
        raise HTTPException(status_code=404, detail="Event tidak ditemukan")
    
    # Jika sukses, kembalikan pesan berhasil
    return {"message": f"Event dengan ID {event_id} berhasil dihapus"}

# Fungsi untuk GET ALL Events
def get_all_events(db: Session):
    return event_repo.get_events(db)

# Fungsi untuk UPDATE Event
def modify_event(db: Session, event_id: int, event_data: EventUpdate):
    # Cek dulu apakah datanya ada
    existing_event = event_repo.get_event_by_id(db, event_id)
    if not existing_event:
        raise HTTPException(status_code=404, detail="Event tidak ditemukan")
    
    # Validasi tambahan: Kalau user mencoba update nama, pastikan tidak kosong
    if event_data.name is not None and not event_data.name.strip():
        raise HTTPException(status_code=400, detail="Nama event tidak boleh kosong!")
        
    # Panggil fungsi update dari repository
    updated_event = event_repo.update_event(db, event_id, event_data)
    return updated_event

# ... lanjut fungsi get_all, modify, dan remove mengikuti pola Role_Service