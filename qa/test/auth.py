from httpx import AsyncClient


async def test_auth_headers(client: AsyncClient):
    assert "authorization" in client.headers.keys()
