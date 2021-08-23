from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Kevin",
        "age": "18",
    }
}


class Student(BaseModel):
    name: str
    age: int

# Get method


@app.get("/")
def index():
    return {"name": "First Data"}

# Path parameter


@app.get("/students/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view", gt=0)):
    return students[student_id]

# Query parameter


@app.get("/get_by_name")
def get_student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

# Post Method


@app.post("/create_student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student Exists"}

    students[student_id] = student
    return students[student_id]
