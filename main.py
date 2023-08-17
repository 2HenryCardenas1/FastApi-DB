from fastapi import FastAPI

from config.database import base, engine, session
from models.movie import Movie

app = FastAPI()

app.title = "Fast Api whit Data base"
app.description = "This is a very fancy project, with auto docs for the API and everything"
app.version = "0.0.1"


# Create all tables in the database
base.metadata.create_all(bind=engine)



@app.get("/")
def read_root():
    return {"Hello": "World"}