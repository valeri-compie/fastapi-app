from fastapi import HTTPException, status


class CredentialsError(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Failed to verify credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
