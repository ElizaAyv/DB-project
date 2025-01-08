from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ConferenceCreate, ConferenceResponse
from app.crud import (
    create_conference,
    get_conference,
    get_conferences,
    update_conference,
    delete_conference,
)

router = APIRouter(prefix="/conferences", tags=["conferences"])

@router.post("/conferences/", response_model=ConferenceResponse, status_code=201)
def create_conference_route(conference: ConferenceCreate, db: Session = Depends(get_db)):
    return create_conference(db, conference)

@router.get("/conferences/{conference_id}", response_model=ConferenceResponse)
def get_conference_route(conference_id: int, db: Session = Depends(get_db)):
    db_conference = get_conference(db, conference_id)
    if not db_conference:
        raise HTTPException(status_code=404, detail="Conference not found")
    return db_conference

@router.get("/conferences/", response_model=list[ConferenceResponse])
def get_conferences_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_conferences(db, skip, limit)

@router.put("/conferences/{conference_id}", response_model=ConferenceResponse)
def update_conference_route(conference_id: int, conference: ConferenceCreate, db: Session = Depends(get_db)):
    updated_conference = update_conference(db, conference_id, conference)
    if not updated_conference:
        raise HTTPException(status_code=404, detail="Conference not found")
    return updated_conference

@router.delete("/conferences/{conference_id}", status_code=204)
def delete_conference_route(conference_id: int, db: Session = Depends(get_db)):
    success = delete_conference(db, conference_id)
    if not success:
        raise HTTPException(status_code=404, detail="Conference not found")
