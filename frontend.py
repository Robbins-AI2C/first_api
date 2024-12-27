import streamlit as st
import requests

# API_URL = "http://127.0.0.1:8000"


st.title("Tactical OPE Toolkit")
st.write("Your best source for Tactical Operational Preparation of the Battlefield")         

# Input text box
input_text = st.text_input("Enter text:")
input_text = input_text.replace(" ", "+")

# Button to submit text
if st.button("Search"):
    if input_text:
        # Send request to FastAPI backend
        backend_url = "http://localhost:8000/search"  # URL of the FastAPI backend
        response = requests.post(backend_url, json={"text": input_text})

        # Process response
        if response.status_code == 200:
            new_text = response.json().get("reversed_text")
            st.success(f"Reversed Text: {new_text}")
        else:
            st.error("Error: Could not process request.")
    else:
        st.warning("Please enter some text.")
        
# Blast Off Button
if st.button("Blast Off!"):
    backend_url = "http://localhost:8000/space"  # URL of the FastAPI backend
    response = requests.post(backend_url)
    
    if response.status_code == 200:
        st.success(response.json().get("message"))
    else:
        st.error("Error: Could not process request.")






