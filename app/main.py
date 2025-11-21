# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS – allow requests from your front-end
origins = [
    "https://your-frontend.vercel.app",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage (temporary)
restaurants = []

# Pydantic model for input
class Restaurant(BaseModel):
    name: str
    rating: int

# GET endpoint – list restaurants
@app.get("/restaurants")
def get_restaurants():
    return restaurants

# POST endpoint – add a restaurant
@app.post("/restaurants")
def add_restaurant(restaurant: Restaurant):
    new_id = len(restaurants) + 1
    restaurant_data = {"id": new_id, "name": restaurant.name, "rating": restaurant.rating}
    restaurants.append(restaurant_data)
    return restaurant_data
