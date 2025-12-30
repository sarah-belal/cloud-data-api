# api/main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Cloud Data API Demo")

# Define a Pydantic model for POST requests
class WeatherRecord(BaseModel):
    city: str
    temperature: float
    condition: str

# GET endpoint: Retrieve weather info
@app.get("/weather")
def get_weather(city: str):
    """
    Retrieve current weather info for a city.
    Example: GET /weather?city=Boston
    """
    return {
        "city": city,
        "temperature": 72,
        "condition": "Sunny"
    }

# POST endpoint: Submit new weather record
@app.post("/weather")
def post_weather(record: WeatherRecord):
    """
    Submit a new weather observation.
    Example: POST /weather with JSON body
    """
    # Here you could save to DB (simulated for demo)
    return {
        "message": "Weather record saved successfully",
        "data": record.dict()
    }

# Optional root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Cloud Data API Demo"}
