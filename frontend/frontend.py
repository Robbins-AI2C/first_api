import streamlit as st
import requests

# API_URL = "http://127.0.0.1:8000"


st.title("Tactical OPE Toolkit")
st.write("Your best source for Tactical Operational Preparation of the Battlefield")         

# Google Search Button
google_input = st.text_input("Google Search:")
if st.button("Google Search"):
    if google_input:
        search_service_url = "https://localhost:8000/search"
        response = requests.post(search_service_url, json={"text": google_input})
        
        if response.status_code == 200:
            pass
        else:
            st.error("Error: Could not process request.")




# Input text box
input_text = st.text_input("Enter test text:")
input_text = input_text.replace(" ", "+")

# Button to submit text
if st.button("Reverse Text"):
    if input_text:
        # Send request to FastAPI backend
        backend_url = "http://localhost:8000/reverse"  # URL of the FastAPI backend
        response = requests.post(backend_url, json={"text": input_text})

        # Process response
        if response.status_code == 200:
            new_text = response.json().get("reversed_text")
            st.success(f"Reversed Text: {new_text}")
        else:
            st.error("Error: Could not process request.")
    else:
        st.warning("Please enter some text.")

