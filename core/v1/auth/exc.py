from fastapi import status
from core.v1.exc import APIException


class CredentialsError(APIException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Failed to verify credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
