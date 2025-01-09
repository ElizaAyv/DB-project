from pydantic import BaseModel, Field
from datetime import date, time
from typing import Optional

class ScientistBase(BaseModel):
    name_surname: str
    country: Optional[str]
    scientific_degree: str
    organization: Optional[str]
    specialization: str

class ScientistCreate(ScientistBase):
    pass

class ScientistResponse(ScientistBase):
    id: int

    class Config:
        orm_mode = True


class ScientistCountResponse(BaseModel):
    conference_name: str
    scientist_count: int

    class Config:
        orm_mode = True


class ConferenceBase(BaseModel):
    name: str
    topic: str
    country: Optional[str] = None
    location: str
    date: date

class ConferenceCreate(ConferenceBase):
    pass

class ConferenceUpdate(ConferenceBase):
    pass

class ConferenceResponse(ConferenceBase):
    id: int

    class Config:
        orm_mode = True


class ParticipationBase(BaseModel):
    scientist_id: int
    conference_id: int
    report_theme: str
    performance_duration: time
    participation_type: Optional[str] = Field(None, max_length=50)

class ParticipationCreate(ParticipationBase):
    pass

class ParticipationUpdate(ParticipationBase):
    participation_type: str


class ParticipationResponse(ParticipationBase):
    id: int

    class Config:
        orm_mode = True