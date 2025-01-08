from sqlalchemy.orm import Session
from app.models import Scientist
from app.schemas import ScientistCreate
from app.models import Conference
from app.schemas import ConferenceCreate
from app.models import Participation
from app.schemas import ParticipationCreate, ParticipationResponse

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

def update_scientist(db: Session, scientist_id: int, updated_data: ScientistCreate):
    db_scientist = db.query(Scientist).filter(Scientist.id == scientist_id).first()
    if not db_scientist:
        return None
    for key, value in updated_data.dict().items():
        setattr(db_scientist, key, value)
    db.commit()
    db.refresh(db_scientist)
    return db_scientist

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

def update_conference(db: Session, conference_id: int, updated_data: ConferenceCreate):
    db_conference = db.query(Conference).filter(Conference.id == conference_id).first()
    if not db_conference:
        return None
    for key, value in updated_data.dict().items():
        setattr(db_conference, key, value)
    db.commit()
    db.refresh(db_conference)
    return db_conference

def delete_conference(db: Session, conference_id: int) -> bool:
    db_conference = db.query(Conference).filter(Conference.id == conference_id).first()
    if db_conference:
        db.delete(db_conference)
        db.commit()
        return True
    return False


def create_participation(db: Session, participation: ParticipationCreate) -> Participation:
    db_participation = Participation(**participation.dict())
    db.add(db_participation)
    db.commit()
    db.refresh(db_participation)
    return db_participation

def get_participation(db: Session, participation_id: int) -> Participation:
    return db.query(Participation).filter(Participation.id == participation_id).first()

def get_participations(db: Session, skip: int = 0, limit: int = 10) -> list[Participation]:
    return db.query(Participation).offset(skip).limit(limit).all()

def update_participation(db: Session, participation_id: int, updated_data: ParticipationCreate) -> Participation:
    db_participation = get_participation(db, participation_id)
    if not db_participation:
        return None
    for key, value in updated_data.dict().items():
        setattr(db_participation, key, value)
    db.commit()
    db.refresh(db_participation)
    return db_participation

def delete_participation(db: Session, participation_id: int) -> bool:
    db_participation = get_participation(db, participation_id)
    if db_participation:
        db.delete(db_participation)
        db.commit()
        return True
    return False