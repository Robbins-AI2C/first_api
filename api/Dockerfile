# Dockerfile Template by Andrew Robbins 

# This is the Dockerfile for an api running FastAPI

# Create the base image (common are Ubuntu or Python)
FROM python:3.12-slim

# Create the working directory inside the container
WORKDIR /app

# Copy the contents of the local app's directory to the container's working directory
COPY . /app

RUN pip install fastapi[all] requests

CMD ["uvicorn", "api_v2:app", "--host", "0.0.0.0", "--port", "8000"]