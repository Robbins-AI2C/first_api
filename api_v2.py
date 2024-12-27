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

@app.post("/space")
def space():
    return {"message": "Let's go to the moon!"}

@app.get("/space")
def space():
    return {"message": "Let's go to the moon!"}

@app.post("/search", response_model=SearchResults)
def process_google_search(input_data: SearchInput):
    """
    Reach out to reverse text function
    """
    reverse_text_function_url = "http://localhost:8001/reverse"
    response = requests.post(reverse_text_function_url, json={"text": input_data.text})
    
    if response.status_code == 200:
        reversed_text = response.json().get("reversed_text")
        return {"reversed_text": reversed_text}
    else:
        return {"error": "microservice is down"}


