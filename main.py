from fastapi import FastAPI
from fastapi.openapi.models import OpenAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/health")
def welcome_health():
    return {"OK"}

@app.post("/phones", status_code= 201 )
def create_user


















