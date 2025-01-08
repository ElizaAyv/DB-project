from sqlalchemy.orm import Session
from app.models import Scientist
from app.schemas import ScientistCreate
from app.models import Conference
from app.schemas import ConferenceCreate

def create_scientist(db: Session, scientist: ScientistCreate) -> Scientist:
    db_scientist = Scientist(**scientist.dict())
    db.add(db_scientist)
    db.commit()
    db.refresh(db_scientist)
    return db_scientist

def get_scientist(db: Session, scientist_id: int) -> Scientist:
    return db.query(Scientist).filter(Scientist.id == scientist_id).first()

def get_scientists(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Scientist).offset(skip).limit(limit).all()

def delete_scientist(db: Session, scientist_id: int) -> bool:
    db_scientist = db.query(Scientist).filter(Scientist.id == scientist_id).first()
    if db_scientist:
        db.delete(db_scientist)
        db.commit()
        return True
    return False


def create_conference(db: Session, conference: ConferenceCreate) -> Conference:
    db_conference = Conference(**conference.dict())
    db.add(db_conference)
    db.commit()
    db.refresh(db_conference)
    return db_conference

def get_conference(db: Session, conference_id: int) -> Conference:
    return db.query(Conference).filter(Conference.id == conference_id).first()

def get_conferences(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Conference).offset(skip).limit(limit).all()

def delete_conference(db: Session, conference_id: int) -> bool:
    db_conference = db.query(Conference).filter(Conference.id == conference_id).first()
    if db_conference:
        db.delete(db_conference)
        db.commit()
        return True
    return False
