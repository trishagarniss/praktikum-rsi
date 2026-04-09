from sqlmodel import Session, select
from datetime import datetime
from src.backend.database.schema.models import Event
from src.backend.dto.event_dto import EventCreate, EventUpdate

# 1. Saat Membuat Event Baru
def create_event(db: Session, event_data: EventCreate):
    new_event = Event.model_validate(event_data)
    
    # Isi waktu saat ini sebelum disimpan
    new_event.created_at = datetime.now()
    new_event.updated_at = datetime.now()
    
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

# 2. Saat Memperbarui Event Lama
def update_event(db: Session, event_id: int, event_data: EventUpdate):
    db_event = db.get(Event, event_id)
    if db_event:
        event_dict = event_data.model_dump(exclude_unset=True)
        for key, value in event_dict.items():
            setattr(db_event, key, value)
            
        # Catat waktu pembaruan
        db_event.updated_at = datetime.now()
        
        db.add(db_event)
        db.commit()
        db.refresh(db_event)
        return db_event
    return None

def get_events(db: Session):
    return db.exec(select(Event)).all()

def get_event_by_id(db: Session, event_id: int):
    return db.get(Event, event_id)

def delete_event(db: Session, event_id: int):
    db_event = db.get(Event, event_id)
    if db_event:
        db.delete(db_event)
        db.commit()
        return True
    return False