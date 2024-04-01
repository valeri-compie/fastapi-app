from fastapi import status

from core.v1.exc import APIException


class CredentialsException(APIException):
    def __init__(self, auth_value: str) -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": auth_value},
        )


class UnauthorizedException(APIException):
    def __init__(self, auth_value: str) -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not enough permissions",
            headers={"WWW-Authenticate": auth_value},
        )


class InactiveUserException(APIException):
    def __init__(self) -> None:
        super().__init__(status_code=400, detail="Inactive user")
