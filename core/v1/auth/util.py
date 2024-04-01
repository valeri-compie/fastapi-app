from datetime import datetime, timedelta, timezone

from jose import jwt as jwt_
from passlib.context import CryptContext

from core.v1.config import config


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_hash(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_hash(password):
    return pwd_context.hash(password)


def encode_jwt(claims: dict):
    exp = datetime.now(timezone.utc) + timedelta(minutes=config.JWT_EXP)
    jwt = jwt_.encode(
        claims={**claims, "exp": exp},
        key=config.JWT_KEY,
        algorithm=config.JWT_ALG,
    )
    return jwt
