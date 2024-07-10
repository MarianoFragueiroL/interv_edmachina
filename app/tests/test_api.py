import pytest
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def create_subject(name):
    subject_data = {
        "name": name
    }
    response = client.post("/api/subjects/", json=subject_data)
    assert response.status_code == 200
    return response.json()["id"]

def test_create_subject_200():
    subject_data = {
        "name": "Mathematics",
    }
    response = client.post("/api/subjects/", json=subject_data)
    assert response.status_code == 200
    assert response.json()["name"] == subject_data["name"]
    return response.json()["id"]

def test_get_all_students():
    response = client.get("/api/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_student_200():
    student_data =  {
            "name": "John test",
            "email": "john@example.com",
            "address": "123 Main St",
            "phone": "555-1234",
            "career": "Engineering",
            "subject_repeats": 0,
            "subjects": [4, 5, 6, 10]
        }
    response = client.post("/api/students/", json=student_data)
    assert response.status_code == 200
    assert response.json()["name"] == student_data["name"]
    return response.json()["id"]

def test_create_student_400_invalid_email():
    student_data = {
        "name": "John Doe 1",
        "email": "invalid-email",
        "address": "123 Main St",
        "phone": "555-1234",
        "career": "Engineering",
        "subject_repeats": 0,
        "subjects": [4, 5, 6, 10]
    }
    response = client.post("/api/students/", json=student_data)
    assert response.status_code == 400

def test_update_student_200():
    subject_ids = [create_subject(f"Subject {i}") for i in range(1, 5)]
    student_id = test_create_student_200()
    update_data = {
        "name": "John Doe 2",
        "email": "john.doe2@example.com",
        "address": "456 Main St",
        "phone": "555-5678",
        "career": "Mathematics",
        "subject_repeats": 1,
        "subjects": [4, 5, 6, 10]
    }
    response = client.put(f"/api/students/{student_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == update_data["name"]


def test_delete_student_200():
    student_id = test_create_student_200()
    response = client.delete(f"/api/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Student deleted successfully"


def test_get_all_subjects():
    response = client.get("/api/subjects/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_subject_200():
    subject_data = {
        "name": "Mathematics",
    }
    response = client.post("/api/subjects/", json=subject_data)
    assert response.status_code == 200
    assert response.json()["name"] == subject_data["name"]
    return response.json()["id"]

def test_create_subject_400_missing_field():
    subject_data = {
        "namee": "Mathematics"
    }
    response = client.post("/api/subjects/", json=subject_data)
    assert response.status_code == 400

def test_delete_subject_200():
    subject_id = test_create_subject_200()
    print('subject_id: ',subject_id)
    response = client.delete(f"/api/subjects/{subject_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Subject deleted successfully"

