from fastapi import HTTPException
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.v1.user import service
from core.v1.database import require as db_require


async def target_user(
    user_id: int,
    db: AsyncSession = Depends(db_require.db_session),
):
    user = await service.select(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404)
    yield user
