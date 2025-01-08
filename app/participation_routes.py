from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ParticipationCreate, ParticipationResponse
from app.crud import (
    create_participation,
    get_participation,
    get_participations,
    update_participation,
    delete_participation
)

router = APIRouter(prefix="/participation", tags=["participation"])

@router.post("/participations/", response_model=ParticipationResponse, status_code=201)
def create_participation_route(participation: ParticipationCreate, db: Session = Depends(get_db)):
    return create_participation(db, participation)

@router.get("/participations/{participation_id}", response_model=ParticipationResponse)
def get_participation_route(participation_id: int, db: Session = Depends(get_db)):
    db_participation = get_participation(db, participation_id)
    if not db_participation:
        raise HTTPException(status_code=404, detail="Participation not found")
    return db_participation

@router.get("/participations/", response_model=list[ParticipationResponse])
def get_participations_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_participations(db, skip, limit)

@router.put("/participations/{participation_id}", response_model=ParticipationResponse)
def update_participation_route(participation_id: int, updated_data: ParticipationCreate, db: Session = Depends(get_db)):
    db_participation = update_participation(db, participation_id, updated_data)
    if not db_participation:
        raise HTTPException(status_code=404, detail="Participation not found")
    return db_participation

@router.delete("/participations/{participation_id}", status_code=204)
def delete_participation_route(participation_id: int, db: Session = Depends(get_db)):
    success = delete_participation(db, participation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Participation not found")
