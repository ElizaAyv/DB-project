from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Scientist, Participation
from app.schemas import ScientistCreate, ScientistResponse
from app.crud import (
    create_scientist,
    get_scientist,
    get_scientists,
    update_scientist,
    delete_scientist,
)

router = APIRouter(prefix="/scientists", tags=["scientists"])

@router.post("/", response_model=ScientistResponse, status_code=201)
def create_scientist_route(scientist: ScientistCreate, db: Session = Depends(get_db)):
    return create_scientist(db, scientist)

@router.get("/", response_model=list[ScientistResponse])
def get_scientists_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_scientists(db, skip, limit)

@router.get("/{scientist_id}", response_model=ScientistResponse)
def get_scientist_route(scientist_id: int, db: Session = Depends(get_db)):
    db_scientist = get_scientist(db, scientist_id)
    if not db_scientist:
        raise HTTPException(status_code=404, detail="Scientist not found")
    return db_scientist

@router.put("/scientists/{scientist_id}", response_model=ScientistResponse)
def update_scientist_route(scientist_id: int, scientist: ScientistCreate, db: Session = Depends(get_db)):
    updated_scientist = update_scientist(db, scientist_id, scientist)
    if not updated_scientist:
        raise HTTPException(status_code=404, detail="Scientist not found")
    return updated_scientist

@router.delete("/{scientist_id}", status_code=204)
def delete_scientist_route(scientist_id: int, db: Session = Depends(get_db)):
    success = delete_scientist(db, scientist_id)
    if not success:
        raise HTTPException(status_code=404, detail="Scientist not found")

#scientists in the conference (Join)
@router.get("/by_conference/{conference_id}", response_model=list[ScientistResponse])
def get_scientists_by_conference(conference_id: int, db: Session = Depends(get_db)):
    scientists = (
        db.query(Scientist)
        .join(Participation, Scientist.id == Participation.scientist_id)
        .filter(Participation.conference_id == conference_id)
        .all()
    )
    if not scientists:
        raise HTTPException(status_code=404, detail="No scientists found for this conference")
    return scientists
