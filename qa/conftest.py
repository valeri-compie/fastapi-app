import pytest_asyncio
from httpx import ASGITransport
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from fastapi import FastAPI

from core.v1.database.service import create_tables
from core.v1.database.service import delete_tables
from core.v1.config import config


@pytest_asyncio.fixture(scope="session")
async def database():
    assert "testing" in config.POSTGRES_DSN
    await delete_tables()
    await create_tables()
    yield
    await delete_tables()


@pytest_asyncio.fixture(scope="session")
async def transport(database):
    from core.v1.app import app

    async with LifespanManager(app) as manager:
        yield ASGITransport(manager.app)


@pytest_asyncio.fixture
async def client(transport: FastAPI):
    client = AsyncClient(transport=transport, base_url="http://")
    async with client:
        yield client
