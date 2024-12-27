from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI()

# Define a request model
class TextInput(BaseModel):
    text: str

# Define a response model
class TextResponse(BaseModel):
    reversed_text: str

@app.post("/reverse", response_model=TextResponse)
def reverse_text(input_data: TextInput):
    """
    Reverse the input text and return the result.
    """
    reversed_text = input_data.text[::-1]
    return {"reversed_text": reversed_text}