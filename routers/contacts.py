from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas
import crud
import database
from typing import List

router = APIRouter()

@router.get("/contacts/", response_model=List[schemas.Contact])
def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_contacts(db, skip=skip, limit=limit)

@router.post("/contacts/", response_model=schemas.Contact)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(database.get_db)):
    return crud.create_contact(db=db, contact=contact)
