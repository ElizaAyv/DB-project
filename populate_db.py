import requests
from faker import Faker
from datetime import time
import random

BASE_URL = "http://127.0.0.1:8000"

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

def populate_participations(n=100):
    scientist_ids = [s["id"] for s in requests.get(f"{BASE_URL}/scientists/").json()]
    conference_ids = [c["id"] for c in requests.get(f"{BASE_URL}/conferences/").json()]

    for _ in range(n):
        participation_data = {
            "scientist_id": faker.random_element(scientist_ids),
            "conference_id": faker.random_element(conference_ids),
            "report_theme": faker.catch_phrase(),
            "performance_duration": faker.time_object().strftime("%H:%M:%S"),
            "participation_type": faker.random_element(["Oral", "Poster", "Workshop"]),
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
