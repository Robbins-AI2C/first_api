from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

# Define a request model
class SearchInput(BaseModel):
    text: str

# Define a response model
class SearchResults(BaseModel):
    reversed_text: str


# Create FastAPI app
app = FastAPI()

# Set up CORS middleware and origin website/IP list
origins = [
    "http://localhost:8501", # Frontend
    "http://localhost:8001", # reverse_text microservice
    "http://localhost:8002", # google_search microservice
    # Add more origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This creates the endpoint for the API's splash page (home page)
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/search")
def process_google_search(input_data: SearchInput):
    google_search_microservice_url = "http://localhost:8002/search"
    response = requests.post(google_search_microservice_url, json={"text": input_data.text})
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "microservice is down"}
