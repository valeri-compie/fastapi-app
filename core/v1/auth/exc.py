from core.v1.exc import AuthorizationError


class CredentialsError(AuthorizationError):
    detail = "Failed to verify credentials"
    headers = {"WWW-Authenticate": "Bearer"}
