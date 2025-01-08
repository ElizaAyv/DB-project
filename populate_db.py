import requests
from faker import Faker
import random

BASE_URL = "http://127.0.0.1:8000"  # Base URL for your FastAPI app

faker = Faker()


def populate_scientists(n=200):
    for _ in range(n):
        scientist_data = {
            "name_surname": faker.name(),
            "country": faker.country(),
            "scientific_degree": random.choice(["PhD", "MSc", "BSc"]),
            "organization": faker.company(),
            "specialization": faker.job()
        }
        response = requests.post(f"{BASE_URL}/scientists/", json=scientist_data)
        if response.status_code == 201:
            print(f"Scientist created: {response.json()}")
        else :
            print(f"Failed to create scientist: {response.text}")


def populate_conferences(n=50):
    for _ in range(n):
        conference_data = {
            "name": faker.catch_phrase(),
            "topic": faker.job(),  #sentences will look unrealistic
            "country": faker.country(),
            "location": faker.city(),
            "date": faker.date_between(start_date='-2y', end_date='+1y').isoformat(),
        }
        response = requests.post(f"{BASE_URL}/conferences/", json=conference_data)
        if response.status_code == 201:
            print(f"Conference created: {response.json()}")
        else:
            print(f"Failed to create conference: {response.text}")


def populate_participations(n=200):
    scientist_ids = [s["id"] for s in requests.get(f"{BASE_URL}/scientists/").json()]
    conference_ids = [c["id"] for c in requests.get(f"{BASE_URL}/conferences/").json()]

    for _ in range(n):
        participation_data = {
            "scientist_id": random.choice(scientist_ids),
            "conference_id": random.choice(conference_ids),
            "report_theme": faker.sentence(), #TODO make more realistic, eext_word_list or smth
            "performance_duration": random.choice(), #TODO find duration method
            "participation_type": random.choice(["Speaker", "Attendee", "Organizer"])
        }
        response = requests.post(f"{BASE_URL}/participations/", json=participation_data)
        if response.status_code == 201:
            print(f"Participation created: {response.json()}")
        else:
            print(f"Failed to create participation: {response.text}")


if __name__ == "__main__":
    populate_scientists()
    populate_conferences()
    populate_participations()
