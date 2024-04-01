from sqlalchemy.ext.asyncio import AsyncSession

from core.v1.model import ORMModel
from core.v1.database.core import engine
from core.v1.config import config
from core.v1.user.service import insert
from core.v1.user.model import UserCreate


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(ORMModel.metadata.create_all)
    await engine.dispose()


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(ORMModel.metadata.drop_all)
    await engine.dispose()


async def create_default_user():
    payload = UserCreate(
        username=config.DEFAULT_USERNAME,
        password=config.DEFAULT_PASSWORD,
    )
    async with AsyncSession(bind=engine) as session:
        await insert(db=session, payload=payload)
