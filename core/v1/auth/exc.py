from core.v1.exc import AuthorizationError


class CredentialsError(AuthorizationError):
    """
    TODO: fix this exception
    """

    detail = "Failed to verify credentials"
    headers = {"WWW-Authenticate": "Bearer"}
