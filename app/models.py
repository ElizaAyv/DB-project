from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database import Base

class Scientist(Base):
    __tablename__ = "scientist"

    id = Column(Integer, primary_key=True)  
    name_surname = Column(String(100), nullable=False)  
    country = Column(String(50))  
    scientific_degree = Column(String(50), nullable=False)  
    organization = Column(String(100)) 
    specialization = Column(String(50), nullable=False)  

    def __repr__(self):
        return f"<Scientist(name_surname='{self.name_surname}', country='{self.country}')>"


class Conference(Base):
    __tablename__ = "conference"

    id = Column(Integer, primary_key=True) 
    name = Column(String(100))
    topic = Column(String(100), nullable=False) 
    country = Column(String(50)) 
    location = Column(String(100), nullable=False)
    date = Column(Date, nullable=False) 

    def __repr__(self):
        return f"<Conference(name='{self.name}', topic='{self.topic}', date='{self.date}')>"


class Participation(Base):
    __tablename__ = "participation"

    id = Column(Integer, primary_key=True) 
    scientist_id = Column(Integer, ForeignKey("scientist.id"), nullable=False)  
    conference_id = Column(Integer, ForeignKey("conference.id"), nullable=False)  
    report_theme = Column(String(100), nullable=False) 
    performance_duration = Column(Time, nullable=False)  
    participation_type = Column(String(50))  

    scientist = relationship("Scientist", backref="participations")
    conference = relationship("Conference", backref="participations")

    def __repr__(self):
        return f"<Participation(scientist_id='{self.scientist_id}', conference_id='{self.conference_id}')>"
