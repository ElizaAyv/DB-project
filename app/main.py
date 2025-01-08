from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.scientist_routes import router as scientist_router
from app.conference_routes import router as conference_router

DB_NAME = "scientific_conference"
DB_USER = "postgres"
DB_PASSWORD = "89793238"
DB_HOST = "localhost"
DB_PORT = 5432
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

app.include_router(scientist_router, prefix="/api")
app.include_router(conference_router, prefix="/api")

