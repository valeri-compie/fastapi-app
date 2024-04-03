from datetime import datetime
from datetime import timedelta
from datetime import timezone

from jose import jwt as jwt_
from passlib.context import CryptContext

from core.v1.config import config


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_hash(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)


def create_hash(plain: str):
    return pwd_context.hash(plain)


def encode_jwt(claims: dict):
    expire = datetime.now(timezone.utc) + timedelta(minutes=config.JWT_EXP)
    return jwt_.encode({**claims, "exp": expire}, config.JWT_KEY, config.JWT_ALG)
