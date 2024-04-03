from fastapi import HTTPException
from fastapi import status


class APIError(HTTPException): ...


class AuthorizationError(APIError):
    def __init__(self) -> None:
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED)
