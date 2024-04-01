from httpx import AsyncClient

from core.v1.config import config
from core.v1.auth.model import Token


async def test_auth_headers(client: AsyncClient):
    assert "authorization" in client.headers.keys()


async def test_auth_login(client: AsyncClient):
    resp = await client.post("/token/", data={"username": config.DEFAULT_USERNAME, "password": config.DEFAULT_PASSWORD})
    assert resp.status_code == 201
    Token(**resp.json())
