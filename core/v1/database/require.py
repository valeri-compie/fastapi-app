from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession

from core.v1.database.core import engine


async def db_engine():
    yield engine
    await engine.dispose()


async def db_session(engine: AsyncEngine = Depends(db_engine)):
    async with AsyncSession(bind=engine) as session:
        yield session
