from sqlmodel import Session
from src.backend.services import event_service
from src.backend.dto.event_dto import EventCreate, EventUpdate

# 1. CREATE
def create_event_controller(event: EventCreate, db: Session):
    return event_service.add_new_event(db=db, event_data=event)

# 2. READ ALL
def get_all_events_controller(db: Session):
    return event_service.get_all_events(db=db)

# 3. READ BY ID
def get_event_by_id_controller(event_id: int, db: Session):
    return event_service.get_event(db=db, event_id=event_id)

# 4. UPDATE
def update_event_controller(event_id: int, event: EventUpdate, db: Session):
    return event_service.modify_event(db=db, event_id=event_id, event_data=event)

# 5. DELETE
def delete_event_controller(event_id: int, db: Session):
    return event_service.remove_event(db=db, event_id=event_id)