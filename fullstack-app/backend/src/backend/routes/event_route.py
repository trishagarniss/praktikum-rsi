from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.backend.database.connection import get_session
from src.backend.dto.event_dto import EventCreate, EventUpdate, EventResponse
from src.backend.controllers import event_controller
from typing import List

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("/", response_model=EventResponse, status_code=201)
def create_event(event: EventCreate, db: Session = Depends(get_session)):
    return event_controller.create_event_controller(event, db)

@router.get("/", response_model=List[EventResponse])
def read_events(db: Session = Depends(get_session)):
    return event_controller.get_all_events_controller(db)

@router.get("/{event_id}", response_model=EventResponse)
def read_event(event_id: int, db: Session = Depends(get_session)):
    return event_controller.get_event_by_id_controller(event_id, db)

@router.put("/{event_id}", response_model=EventResponse)
def update_event(event_id: int, event: EventUpdate, db: Session = Depends(get_session)):
    return event_controller.update_event_controller(event_id, event, db)

@router.delete("/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_session)):
    return event_controller.delete_event_controller(event_id, db)