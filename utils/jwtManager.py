from fastapi import HTTPException, Request
from jwt import decode, encode

_SECRET_KEY = "secret"

class JwtManager:
    def create_token(payload):
        return encode(payload, key=_SECRET_KEY, algorithm="HS256")

    def validate_token(token) -> dict:
        data: dict = decode(token, _SECRET_KEY, algorithms="HS256")
        return data
