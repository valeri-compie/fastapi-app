"""
authentication as descibed in the official tutorial
https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/
"""

from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={
        "me": "Read information about the current user.",
        "items": "Read items.",
    },
)
