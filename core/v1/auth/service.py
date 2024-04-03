from sqlalchemy.ext.asyncio import AsyncSession

from core.v1.auth.util import verify_hash
from core.v1.user import service as user_service


async def authenticate(db: AsyncSession, username: str, password: str):
    user = await user_service.select_by_username(db, username)
    if not user or not verify_hash(password, user.password):
        return False
    return user
