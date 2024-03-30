from core.v1.model import ORMModel
from core.v1.database.core import engine


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(ORMModel.metadata.create_all)
    await engine.dispose()


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(ORMModel.metadata.drop_all)
    await engine.dispose()
