# Dockerfile Template by Andrew Robbins 

# This is the Dockerfile for a frontend application running Streamlit

# Create the base image (common are Ubuntu or Python)
FROM python:3.12-slim

# Create the working directory inside the container
WORKDIR /app

# Copy the contents of the local app's directory to the container's working directory
COPY . /app

RUN pip install streamlit 

