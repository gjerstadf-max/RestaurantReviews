from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    place_name = Column(String)
    source = Column(String)
    rating = Column(Float)
    text = Column(Text)
    date = Column(String)
