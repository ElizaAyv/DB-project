from pydantic import BaseModel
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


class ConferenceBase(BaseModel):
    title: str
    location: str
    date: str  # Assuming you're using a string for date in "YYYY-MM-DD" format
    topic: Optional[str] = None

class ConferenceCreate(ConferenceBase):
    pass

class ConferenceResponse(ConferenceBase):
    id: int

    class Config:
        orm_mode = True


class ParticipationBase(BaseModel):
    scientist_id: int
    conference_id: int
    role: Optional[str] = None

class ParticipationCreate(ParticipationBase):
    pass

class ParticipationResponse(ParticipationBase):
    id: int

    class Config:
        orm_mode = True