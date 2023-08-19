from typing import List

from fastapi import APIRouter, Depends, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from config.database import session
from middlewares.jwt_bearer import JWTBearer
from models.movie import Movie as MovieModel
from schemas.movie import Movie
from services.movie import MovieService

movie_router = APIRouter()


def not_found():
    return JSONResponse(status_code=404, content={"message": "Movie not found"})


@movie_router.post("/movie", tags=["movie"], response_model=Movie)
def create_movie(movie: Movie) -> List[Movie]:
    db = session()
    MovieService(db).create_movie(movie)
    return JSONResponse(
        status_code=201, content={"message": "Movie created successfully"}
    )


@movie_router.get(
    "/movies",
    tags=["movie"],
    response_model=List[Movie],
    dependencies=[Depends(JWTBearer())],
)
def get_movies() -> List[Movie]:
    db = session()
    result = MovieService(db).get_movies()

    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get("/movie/{movie_id}", tags=["movie"], response_model=Movie)
def get_movie(movie_id: int) -> Movie:
    db = session()
    movie = MovieService(db).get_movie(movie_id)
    if not movie:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})

    return JSONResponse(status_code=200, content=jsonable_encoder(movie))


@movie_router.get("/movie/", tags=["movie"], response_model=List[Movie])
def get_movie_by_category(
    category: str = Query(min_length=1, max_length=50)
) -> List[Movie]:
    db = session()
    results = MovieService(db).get_movie_by_category(category)

    if not results:
        return JSONResponse(status_code=404, content={"message": "Category not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(results))


@movie_router.put("/movie/{id}", tags=["movie"], response_model=dict)
def update_movie(id: int, movie: Movie) -> dict:
    db = session()
    query = MovieService(db).get_movie(id)
    if not query:
        return not_found()
    MovieService(db).update_movie(id, movie)

    return JSONResponse(status_code=201, content={"message": "Movie updated succses"})


@movie_router.delete("/movie/{id}", tags=["movie"])
def delete_movie(id: int):
    db = session()
    query = MovieService(db).get_movie(id)
    if not query:
        return not_found()
    MovieService(db).delete_movie(id)

    return JSONResponse(status_code=200, content={"message": "Movie deleted"})
