from fastapi import FastAPI

from config.database import base, engine
from middlewares.error_handler import ErrorHandler
from routers.auth import auth_router
from routers.movie import movie_router

app = FastAPI()

app.title = "Fast Api whit Data base"
app.description = (
    "This is a very fancy project, with auto docs for the API and everything"
)
app.version = "0.0.1"


app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(auth_router)

# Create all tables in the database
base.metadata.create_all(bind=engine)
