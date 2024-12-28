# Template for creating a FastAPI application by Andrew Robbins

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import subprocess

API_KEY = "AIzaSyDdL5XJQbomYDTvyPvfiDMD0g3Sm3n3xSc"

# Define a request model
class SearchInput(BaseModel):
    text: str

# Define a response model
    


# Initialize FastAPI
app = FastAPI(debug=True)

origins = [
    "http://localhost:8000", # Frontend
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
async def home_page():
    return {"message": "You shouldn't be here!"} # Always in a dictionary/JSON format

@app.post("/search")
def process_google_search(input_data: SearchInput):
    text_search = input_data.text
    google_search_url = "https://places.googleapis.com/v1/places:searchText"
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress"
    }
    data = {
        'textQuery': text_search,
        "includePureServiceAreaBusinesses": True
    }
    
    response = requests.post(google_search_url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}




