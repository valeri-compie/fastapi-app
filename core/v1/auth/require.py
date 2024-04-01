from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import ValidationError

from core.v1.user.model import UserDetail
from core.v1.user import service as user_service
from core.v1.database.require import db_session
from core.v1.auth.model import TokenData
from core.v1.config import config
from core.v1.auth.exc import CredentialsError


oauth2 = OAuth2PasswordBearer(tokenUrl="token")


async def bearer(
    db: AsyncSession = Depends(db_session),
    token: str = Depends(oauth2),
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


async def active_user(
    user: UserDetail = Depends(bearer),
):
    if user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user
