import pytest_asyncio
from httpx import ASGITransport
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from fastapi import FastAPI

from core.v1.auth.model import Token
from core.v1.database.service import create_tables
from core.v1.database.service import delete_tables
from core.v1.config import config


@pytest_asyncio.fixture(scope="session")
async def setup_database():
    assert "testing" in config.POSTGRES_DSN
    await delete_tables()
    await create_tables()
    yield
    await delete_tables()


@pytest_asyncio.fixture(scope="session")
async def transport(setup_database):
    from core.v1.app import app

    async with LifespanManager(app) as manager:
        yield ASGITransport(manager.app)


@pytest_asyncio.fixture(scope="session")
async def client(transport: FastAPI):
    client = AsyncClient(transport=transport, base_url="http://")
    async with client:
        yield client


@pytest_asyncio.fixture(scope="session")
async def user_client(client: AsyncClient):
    resp = await client.post("/auth/login", data={"username": config.DEFAULT_USERNAME, "password": config.DEFAULT_PASSWORD})
    data = Token(**resp.json())
    client.headers["Authorization"] = f"Bearer {data.access_token}"
    yield client
