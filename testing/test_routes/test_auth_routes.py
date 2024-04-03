from httpx import AsyncClient

from core.v1.config import config
from core.v1.auth.model import Token


async def test_auth_headers(user_client: AsyncClient):
    assert "authorization" in user_client.headers.keys()


async def test_auth_status(user_client: AsyncClient):
    resp = await user_client.get("/auth/status")
    assert resp.status_code == 200


async def test_auth_login(user_client: AsyncClient):
    resp = await user_client.post("/auth/login", data={"username": config.DEFAULT_USERNAME, "password": config.DEFAULT_PASSWORD})
    assert resp.status_code == 201
    Token(**resp.json())
