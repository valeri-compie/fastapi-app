from typing import Annotated

from fastapi import Depends, Security
from fastapi.security import (
    SecurityScopes,
)
from jose import JWTError
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from core.v1.auth.exc import CredentialsException
from core.v1.auth.exc import UnauthorizedException
from core.v1.auth.exc import InactiveUserException
from core.v1.auth.util import get_token_data
from core.v1.user import service as user_service
from core.v1.auth import oauth2_scheme
from core.v1.user.model import UserDetail
from core.v1.database.require import db_session


async def authorized_user(
    scopes: SecurityScopes,
    db: AsyncSession = Depends(db_session),
    token: str = Depends(oauth2_scheme),
):
    if scopes.scopes:
        auth_value = f'Bearer scope="{scopes.scope_str}"'
    else:
        auth_value = "Bearer"
    try:
        token_data = get_token_data(token=token)
    except (JWTError, ValidationError):
        raise CredentialsException(auth_value=auth_value)
    user = await user_service.select_by_username(db=db, username=token_data.username)
    if user is None:
        raise CredentialsException(auth_value=auth_value)
    for scope in scopes.scopes:
        if scope not in token_data.scopes:
            raise UnauthorizedException(auth_value=auth_value)
    return user


async def get_current_active_user(
    current_user: Annotated[UserDetail, Security(authorized_user, scopes=["me"])],
):
    if current_user.disabled:
        raise InactiveUserException
    return current_user
