from fastapi.testclient import TestClient
from demo import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI Addition API!"}

def test_add_numbers():
    response = client.post("/add", json={"num1": 5.5, "num2": 4.5})
    assert response.status_code == 200
    assert response.json() == {"result": 10.0}

def test_add_numbers_negative():
    response = client.post("/add", json={"num1": -5, "num2": 10})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}

def test_subtract_numbers():
    response = client.post("/subtract", json={"num1": 10.5, "num2": 4.5})
    assert response.status_code == 200
    assert response.json() == {"result": 6.0}

def test_subtract_numbers_negative_result():
    response = client.post("/subtract", json={"num1": 5, "num2": 10})
    assert response.status_code == 200
    assert response.json() == {"result": -5.0}
