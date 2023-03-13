import time
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

items = []

class ModelResponse(BaseModel):
    input: str
    output: str
    time: float

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict", response_model=ModelResponse)
async def predict(input: str) -> ModelResponse:
    start = time.time()
    predicted_val = long_ml_operation(input)
    time_spent = time.time() - start
    response = ModelResponse(
        input = input,
        output = predicted_val,
        time = time_spent,
    )
    return response

def long_ml_operation(input: str) -> str:
    for i in range(3):
        time.sleep(1)
        print("we wait... {} seconds.".format(i+1))
    return input.upper()