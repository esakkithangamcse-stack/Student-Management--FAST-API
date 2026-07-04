import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.session import get_db

client = TestClient(app)

def override_get_db():
    try:
        # Provide a mock db session here if needed
        yield "mock_db_session"
    finally:
        pass

app.dependency_overrides[get_db] = override_get_db

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Student Management API"}

def test_read_students():
    response = client.get("/students/")
    assert response.status_code == 200
    # Add more tests as needed
