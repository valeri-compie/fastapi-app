from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, Security, APIRouter
from fastapi.security import (
    OAuth2PasswordRequestForm,
)
from sqlalchemy.ext.asyncio import AsyncSession

from core.v1.user.model import UserDetail
from core.v1.auth.model import Token
from core.v1.auth.util import create_access_token
from core.v1.auth import service
from core.v1.auth import require
from core.v1.database import require as db_require
from core.v1.auth.config import ACCESS_TOKEN_EXPIRE_MINUTES


router = APIRouter()


@router.post("/")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncSession = Depends(db_require.db_session),
) -> Token:
    user = await service.authenticate_user(db=db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/users/me/", response_model=UserDetail)
async def read_users_me(
    current_user: Annotated[UserDetail, Depends(require.get_current_active_user)],
):
    return current_user
