from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from core.v1.database.require import db_session
from core.v1.auth.model import Token
from core.v1.auth.util import encode_jwt
from core.v1.auth.service import authenticate
from core.v1.auth.exc import CredentialsError

router = APIRouter()


@router.get("/status", response_class=Response)
async def status(db: AsyncSession = Depends(db_session)) -> Token:
    return Response(status_code=200)


@router.post("/login", status_code=201)
async def login(
    form: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
    db: AsyncSession = Depends(db_session),
) -> Token:
    subject = await authenticate(db, form.username, form.password)
    if not subject:
        raise CredentialsError
    encoded = encode_jwt(claims={"sub": str(subject.id)})
    return Token(access_token=encoded, token_type="bearer")
