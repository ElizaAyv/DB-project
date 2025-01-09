from app.database import SessionLocal
from app.models import Conference

db = SessionLocal()

example_tags = [
    {"id": 1, "tags": ["AI", "Quantum Computing"]},
    {"id": 2, "tags": ["Astrophysics", "Space Exploration"]}
]

for tag_data in example_tags:
    conference = db.query(Conference).filter_by(id=tag_data["id"]).first()
    if conference:
        conference.tags = tag_data["tags"]
        db.commit()

print("Tags populated successfully!")
