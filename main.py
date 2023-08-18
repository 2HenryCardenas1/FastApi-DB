from fastapi import  FastAPI
from fastapi.responses import JSONResponse

from config.database import base, engine
from middlewares.error_handler import ErrorHandler

from schemas.user import User
from utils.jwtManager import JwtManager
from routers.movie import movie_router

app = FastAPI()

app.title = "Fast Api whit Data base"
app.description = (
    "This is a very fancy project, with auto docs for the API and everything"
)
app.version = "0.0.1"


app.add_middleware(ErrorHandler)
app.include_router(movie_router)

# Create all tables in the database
base.metadata.create_all(bind=engine)



@app.post("/login", tags=["login"])
def login(user: User):
    if user.email == "admin@admin.com" and user.password == "admin":
        token = JwtManager.create_token({"email": user.email})
        return JSONResponse(
            content={"message": "Login success", "token": token}, status_code=200
        )



