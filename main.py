from typing import List

from fastapi import FastAPI, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from config.database import base, engine, session
from models.movie import Movie as MovieModel
from schemas.movie import Movie

app = FastAPI()

app.title = "Fast Api whit Data base"
app.description = (
    "This is a very fancy project, with auto docs for the API and everything"
)
app.version = "0.0.1"


# Create all tables in the database
base.metadata.create_all(bind=engine)


def not_found():
    return JSONResponse(status_code=404, content={"message": "Movie not found"})


@app.post("/movie", tags=["movie"], response_model=Movie)
def create_movie(movie: Movie) -> List[Movie]:
    db = session()
    new_movie = MovieModel(**movie.model_dump())
    db.add(new_movie)

    db.commit()
    return JSONResponse(
        status_code=201, content={"message": "Movie created successfully"}
    )


@app.get("/movies", tags=["movie"], response_model=List[Movie])
def get_movies() -> List[Movie]:
    db = session()
    movies = jsonable_encoder(db.query(MovieModel).all())

    return JSONResponse(status_code=200, content=movies)


@app.get("/movie/{movie_id}", tags=["movie"], response_model=Movie)
def get_movie(movie_id: int) -> Movie:
    db = session()
    movie = jsonable_encoder(
        db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    )
    if not movie:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})

    return JSONResponse(status_code=200, content=movie)


@app.get("/movie/", tags=["movie"], response_model=List[Movie])
def get_movie_by_category(
    category: str = Query(min_length=1, max_length=50)
) -> List[Movie]:
    db = session()
    results = jsonable_encoder(db.query(MovieModel).filter_by(category=category).all())
    print(results)
    if not results:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})
    return JSONResponse(status_code=200, content=results)


@app.put("/movie/{id}", tags=["movie"], response_model=dict)
def update_movie(id: int, movie: Movie) -> dict:
    db = session()
    query = db.query(MovieModel).filter(MovieModel.id == id).first()

    if not query:
        return JSONResponse(status_code=404, content={"message": "Not found"})

    query.title = movie.title
    query.overview = movie.overview
    query.year = movie.year
    query.rating = movie.rating
    query.category = movie.category

    db.commit()

    return JSONResponse(status_code=201, content={"message": "Movie updated succses"})


@app.delete("/movie/{id}", tags=["movies"])
def delete_movie(id: int):
    db = session()
    query = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not query:
        return not_found()

    db.delete(query)
    db.commit()

    return JSONResponse(status_code=200, content={"message": "Movie deleted"})
