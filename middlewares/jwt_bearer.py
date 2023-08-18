from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer

from utils.jwtManager import JwtManager


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = JwtManager.validate_token(auth.credentials)

        if data["email"] != "admin@admin.com":
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")
