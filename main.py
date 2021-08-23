from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
    1: {
        "name": "Kevin",
        "age": "18",
    }
}


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/students/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view", gt=0)):
    return students[student_id]


@app.get("/get_by_name")
def get_student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}
