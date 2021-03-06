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


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

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

# Put Method


@app.put("/update_student/{student_id}")
def update_student(student_id: int, Student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exists"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    return students[student_id]

# Delete Method


@app.delete("/delete_student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exists"}

    del students[student_id]
    return {"Message": "Student deleted successfully"}
