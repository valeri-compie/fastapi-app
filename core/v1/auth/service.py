from sqlalchemy.ext.asyncio import AsyncSession

from core.v1.user import service as user_service
from core.v1.auth.util import verify_password


async def authenticate_user(db: AsyncSession, username: str, password: str):
    user = await user_service.select_by_username(db=db, username=username)
    if user and verify_password(password, user.password):
        return user
