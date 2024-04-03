from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from jose import jwt
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from core.v1.user.model import UserDetail
from core.v1.user import service as user_service
from core.v1.database.require import db_session
from core.v1.auth.model import TokenData
from core.v1.config import config
from core.v1.auth.exc import CredentialsError


auth_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def jwt_subject(
    db: AsyncSession = Depends(db_session),
    token: str = Depends(auth_schema),
):
    try:
        decode = jwt.decode(token, config.JWT_KEY, algorithms=[config.JWT_ALG])
        claims = TokenData(user_id=decode.get("sub"))
    except (JWTError, ValidationError):
        raise CredentialsError
    holder = await user_service.select(db=db, user_id=claims.user_id)
    if holder is None:
        raise CredentialsError
    return holder


async def active_jwt_subject(
    user: UserDetail = Depends(jwt_subject),
):
    if user.disabled:
        raise CredentialsError
    return user
