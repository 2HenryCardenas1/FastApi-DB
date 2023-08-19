from fastapi import APIRouter
from fastapi.responses import JSONResponse

from schemas.user import User
from utils.jwtManager import JwtManager

auth_router = APIRouter()


@auth_router.post("/login", tags=["login"])
def login(user: User):
    if user.email == "admin@admin.com" and user.password == "admin":
        token = JwtManager.create_token({"email": user.email})
        return JSONResponse(
            content={"message": "Login success", "token": token}, status_code=200
        )
