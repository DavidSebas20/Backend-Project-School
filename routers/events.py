from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas
import crud
import database
from typing import List

router = APIRouter()

@router.get("/events/", response_model=List[schemas.Event])
def read_events(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_events(db, skip=skip, limit=limit)

@router.post("/events/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(database.get_db)):
    return crud.create_event(db=db, event=event)
