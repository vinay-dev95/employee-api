from fastapi.testclient import TestClient
from app.main import app
from app.models import Employee

client = TestClient(app)

def test_add_and_get_employee():
    emp_data = {"empID": 1, "empName": "John", "empFname": "Doe", "empRole": "Developer", "empBG": "O+"}
    response = client.post("/employee", json=emp_data)
    assert response.status_code == 200
    assert response.json()["employee"]["empName"] == "John"

    # Get employee
    response = client.get("/employee/1")
    assert response.status_code == 200
    assert response.json()["empRole"] == "Developer"

def test_get_all_employees():
    response = client.get("/employees")
    assert response.status_code == 200
    assert len(response.json()) >= 1
