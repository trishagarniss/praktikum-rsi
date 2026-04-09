from sqlmodel import Session, select
from datetime import datetime
from src.backend.database.schema.models import Event
from src.backend.dto.event_dto import EventCreate, EventUpdate

# 1. CREATE
def create_event(db: Session, event_data: EventCreate):
    new_event = Event(
        name=event_data.name,
        description=event_data.description,
        quota=event_data.quota,
        started_at=event_data.started_at,
        ended_at=event_data.ended_at,
        # Catat waktu pembuatan secara manual
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

# 2. READ ALL
def get_events(db: Session):
    return db.exec(select(Event)).all()

# 3. READ BY ID
def get_event_by_id(db: Session, event_id: int):
    return db.get(Event, event_id)

# 4. UPDATE
def update_event(db: Session, event_id: int, event_data: EventUpdate):
    db_event = db.get(Event, event_id)
    if db_event:
        db_event.name = event_data.name
        db_event.description = event_data.description
        db_event.quota = event_data.quota
        db_event.started_at = event_data.started_at
        db_event.ended_at = event_data.ended_at
        
        # Perbarui waktu update
        db_event.updated_at = datetime.now()
        
        db.add(db_event)
        db.commit()
        db.refresh(db_event)
        return db_event
    return None

# 5. DELETE
def delete_event(db: Session, event_id: int):
    db_event = db.get(Event, event_id)
    if db_event:
        db.delete(db_event)
        db.commit()
        return True
    return False