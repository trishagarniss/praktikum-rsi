from sqlmodel import Session
from src.backend.services import event_service
from src.backend.dto.event_dto import EventCreate, EventUpdate

def create_event_controller(event_data: EventCreate, db: Session):
    return event_service.add_new_event(db, event_data)

def get_all_events_controller(db: Session):
    return event_service.get_all_events(db)

def get_event_by_id_controller(event_id: int, db: Session):
    return event_service.get_event_detail(db, event_id)

def update_event_controller(event_id: int, event_data: EventUpdate, db: Session):
    return event_service.modify_event(db, event_id, event_data)

def delete_event_controller(event_id: int, db: Session):
    return event_service.remove_event(db, event_id)