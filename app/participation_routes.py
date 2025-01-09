from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ParticipationCreate, ParticipationResponse, ParticipationUpdate
from app.crud import (
    create_participation,
    get_participation,
    get_participations,
    update_participation,
    delete_participation,
    update_participation_type,
)

router = APIRouter(prefix="/participations", tags=["participations"])

@router.post("/", response_model=ParticipationResponse, status_code=201)
def create_participation_route(participation: ParticipationCreate, db: Session = Depends(get_db)):
    return create_participation(db, participation)

@router.get("/", response_model=list[ParticipationResponse])
def get_participations_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_participations(db, skip, limit)

@router.get("/{participation_id}", response_model=ParticipationResponse)
def get_participation_route(participation_id: int, db: Session = Depends(get_db)):
    db_participation = get_participation(db, participation_id)
    if not db_participation:
        raise HTTPException(status_code=404, detail="Participation not found")
    return db_participation

@router.put("/{participation_id}", response_model=ParticipationResponse)
def update_participation_route(participation_id: int, updated_data: ParticipationUpdate, db: Session = Depends(get_db)):
    updated_participation = update_participation(db, participation_id, updated_data)
    if not updated_participation:
        raise HTTPException(status_code=404, detail="Participation not found")
    return updated_participation

@router.delete("/{participation_id}", status_code=204)
def delete_participation_route(participation_id: int, db: Session = Depends(get_db)):
    success = delete_participation(db, participation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Participation not found")

#update participation type
@router.put("/update-participation-type/", response_model=dict)
def update_participation_type_route(keyword: str, new_type: str, db: Session = Depends(get_db)):
    updated_rows = update_participation_type(db, keyword, new_type)
    if updated_rows == 0:
        raise HTTPException(status_code=404, detail="No participations matched the criteria.")
    return {"message": f"{updated_rows} participations updated successfully."}
