from typing import List

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from models.movie import Movie as MovieModel
from schemas.movie import Movie


class MovieService:
    # Dependency Injection of database session in the service class constructor method (Dependency Inversion Principle)
    def __init__(self, db):
        self.db = db

    # Queries

    def get_movies(self) -> List[Movie]:
        result = self.db.query(MovieModel).all()
        return result

    def get_movie(self, movie_id: int) -> Movie:
        query = self.db.query(MovieModel).filter(MovieModel.id == movie_id).first()

        return query

    def get_movie_by_category(self, category: str) -> List[Movie]:
        query = self.db.query(MovieModel).filter(MovieModel.category == category).all()

        return query

    def create_movie(self, movie: Movie) -> List[Movie]:
        new_movie = MovieModel(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()
        return

    def update_movie(self, id: int, movie: Movie) -> dict:
        query = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        query.title = movie.title
        query.overview = movie.overview
        query.year = movie.year
        query.rating = movie.rating
        query.category = movie.category
        self.db.commit()
        return
    
    def delete_movie(self, id: int) :
        query = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        self.db.delete(query)
        self.db.commit()
        return
