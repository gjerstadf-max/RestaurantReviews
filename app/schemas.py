from pydantic import BaseModel

class ReviewBase(BaseModel):
    place_name: str
    source: str
    rating: float
    text: str
    date: str

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    class Config:
        orm_mode = True
