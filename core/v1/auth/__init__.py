"""
authentication as descibed in the official tutorial
https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/
"""

from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={
        "user-select": "Select users",
        "user-create": "Create users",
        "user-update": "Update users",
        "user-delete": "Delete users",
        "me-select": "Select current user",
        "me-update": "Update current user",
        "me-delete": "Delete current user",
    },
)
