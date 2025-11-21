from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Restaurant Reviews API is running!"}
