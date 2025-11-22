from fastapi import FastAPI, HTTPException
from app.models import Employee

app = FastAPI(title="Employee API v1.0.0")

# In-memory "database"
employees = []

@app.post("/employee")
def add_employee(emp: Employee):
    for e in employees:
        if e.empID == emp.empID:
            raise HTTPException(status_code=400, detail="Employee ID already exists")
    employees.append(emp)
    return {"message": "Employee added successfully", "employee": emp}

@app.get("/employee/{empID}")
def get_employee(empID: int):
    for emp in employees:
        if emp.empID == empID:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

@app.get("/employees")
def get_all_employees():
    return employees
