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

