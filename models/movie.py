from sqlalchemy import Column, Float, Integer, String

from config.database import base


class Movie(base) :
    __tablename__ = 'movies'

    id = Column(Integer,primary_key=True, index=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)