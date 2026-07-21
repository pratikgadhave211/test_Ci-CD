from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AdditionRequest(BaseModel):
    num1: float
    num2: float

@app.post("/add")
def add_numbers(request: AdditionRequest):
    return {"result": request.num1 + request.num2}

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Addition API!"}

class SubtractionRequest(BaseModel):
    num1: float
    num2: float

@app.post("/subtract")
def subtract_numbers(request: SubtractionRequest):
    return {"result": request.num1 - request.num2}
