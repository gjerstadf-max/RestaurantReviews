from fastapi import FastAPI
from .database import engine
from . import models

# Create DB tables (if not exist)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Restaurant Reviews API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
