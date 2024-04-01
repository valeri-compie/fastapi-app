from sqlalchemy.ext.asyncio import AsyncSession

from core.v1.auth.util import verify_password
from core.v1.user import service as user_service


async def authenticate_user(db: AsyncSession, username: str, password: str):
    user = await user_service.select_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
