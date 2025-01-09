from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Conference
from app.schemas import ConferenceCreate, ConferenceResponse, ConferenceUpdate, ScientistCountResponse
from app.crud import (
    create_conference,
    get_conference,
    get_conferences,
    update_conference,
    delete_conference,
    get_scientist_count_per_conference,
)

router = APIRouter(prefix="/conferences", tags=["conferences"])

@router.post("/", response_model=ConferenceResponse, status_code=201)
def create_conference_route(conference: ConferenceCreate, db: Session = Depends(get_db)):
    return create_conference(db, conference)

@router.get("/", response_model=list[ConferenceResponse])
def get_conferences_route(
    skip: int = 0,
    limit: int = 10,
    sort_by: str = None,
    sort_order: str = "asc", 
    db: Session = Depends(get_db)
):
    query = db.query(Conference)

    if sort_by:
        if sort_by not in ["name", "date", "country"]:  # Validate allowed fields
            raise HTTPException(status_code=400, detail="Invalid sort field")
        column = getattr(Conference, sort_by, None)
        if sort_order.lower() == "desc":
            query = query.order_by(column.desc())
        else:
            query = query.order_by(column.asc())
    return query.offset(skip).limit(limit).all()

@router.get("/{conference_id}", response_model=ConferenceResponse)
def get_conference_route(conference_id: int, db: Session = Depends(get_db)):
    db_conference = get_conference(db, conference_id)
    if not db_conference:
        raise HTTPException(status_code=404, detail="Conference not found")
    return db_conference

@router.put("/{conference_id}", response_model=ConferenceResponse)
def update_conference_route(conference_id: int, updated_data: ConferenceUpdate, db: Session = Depends(get_db)):
    updated_conference = update_conference(db, conference_id, updated_data)
    if not updated_conference:
        raise HTTPException(status_code=404, detail="Conference not found")
    return updated_conference

@router.delete("/{conference_id}", status_code=204)
def delete_conference_route(conference_id: int, db: Session = Depends(get_db)):
    success = delete_conference(db, conference_id)
    if not success:
        raise HTTPException(status_code=404, detail="Conference not found")


#select conference by country and date
@router.get("/filter/", response_model=list[ConferenceResponse])
def filter_conferences(country: str = None, start_date: str = None, end_date: str = None, db: Session = Depends(get_db)):
    query = db.query(Conference)
    if country:
        query = query.filter(Conference.country == country)
    if start_date:
        query = query.filter(Conference.date >= start_date)
    if end_date:
        query = query.filter(Conference.date <= end_date)
    return query.all()

#count the scientists per conference (Group by)
@router.get("/scientist-count/", response_model=list[ScientistCountResponse])
def get_scientist_count_route(db: Session = Depends(get_db)):
    return [
        {"conference_name": name, "scientist_count": count}
        for name, count in get_scientist_count_per_conference(db)
    ]

