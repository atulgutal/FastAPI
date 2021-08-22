from fastapi import FastAPI, Path

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
def index(student_id: int = Path(None, description="The ID of the student you want to view", gt=0)):
    return students[student_id]
