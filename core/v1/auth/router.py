from datetime import timedelta

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from core.v1.database.require import db_session
from core.v1.auth.model import Token
from core.v1.auth.util import create_access_token
from core.v1.auth.service import authenticate_user
from core.v1.config import config


router = APIRouter()


@router.post("/", status_code=201)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
    db: AsyncSession = Depends(db_session),
) -> Token:
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=config.JWT_EXP)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type="bearer")
