from sqlalchemy.orm import Session
from app.models import Scientist
from app.schemas import ScientistCreate
from app.models import Conference
from app.schemas import ConferenceCreate, ConferenceUpdate
from app.models import Participation
from app.schemas import ParticipationCreate, ParticipationUpdate

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

def create_conference(db: Session, conference_data: ConferenceCreate) -> Conference:
    conference = Conference(**conference_data.dict())
    db.add(conference)
    db.commit()
    db.refresh(conference)
    return conference

def get_conference(db: Session, conference_id: int) -> Conference:
    return db.query(Conference).filter(Conference.id == conference_id).first()

def get_conferences(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Conference).offset(skip).limit(limit).all()

def update_conference(db: Session, conference_id: int, updated_data: ConferenceUpdate) -> Conference:
    conference = db.query(Conference).filter(Conference.id == conference_id).first()
    if not conference:
        return None
    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(conference, key, value)
    db.commit()
    db.refresh(conference)
    return conference

def delete_conference(db: Session, conference_id: int) -> bool:
    conference = db.query(Conference).filter(Conference.id == conference_id).first()
    if not conference:
        return False
    db.delete(conference)
    db.commit()
    return True


def create_participation(db: Session, participation_data: ParticipationCreate) -> Participation:
    participation = Participation(**participation_data.dict())
    db.add(participation)
    db.commit()
    db.refresh(participation)
    return participation

def get_participation(db: Session, participation_id: int) -> Participation:
    return db.query(Participation).filter(Participation.id == participation_id).first()

def get_participations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Participation).offset(skip).limit(limit).all()

def update_participation(db: Session, participation_id: int, updated_data: ParticipationUpdate) -> Participation:
    participation = db.query(Participation).filter(Participation.id == participation_id).first()
    if not participation:
        return None
    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(participation, key, value)
    db.commit()
    db.refresh(participation)
    return participation

def delete_participation(db: Session, participation_id: int) -> bool:
    participation = db.query(Participation).filter(Participation.id == participation_id).first()
    if not participation:
        return False
    db.delete(participation)
    db.commit()
    return True
