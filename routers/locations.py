from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas
import crud
import database
from typing import List

router = APIRouter()

@router.get("/locations/", response_model=List[schemas.Location])
def read_locations(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_locations(db, skip=skip, limit=limit)

@router.post("/locations/", response_model=schemas.Location)
def create_location(location: schemas.LocationCreate, db: Session = Depends(database.get_db)):
    return crud.create_location(db=db, location=location)
