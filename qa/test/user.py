from httpx import AsyncClient

import shortuuid
from core.v1.user.model import UserCreate


async def test_create_a(client: AsyncClient):
    username = shortuuid.uuid()
    password = shortuuid.uuid()
    data = UserCreate(
        username=username,
        password=password,
    )
    resp = await client.post("/users/", json=data.model_dump())
    assert resp.status_code == 201


async def test_create_b(client: AsyncClient):
    username = shortuuid.uuid()
    password = shortuuid.uuid()
    data = UserCreate(
        username=username,
        password=password,
    )
    resp = await client.post("/users/", json=data.model_dump())
    assert resp.status_code == 201


async def test_select(client: AsyncClient):
    resp = await client.get("/users/1")
    assert resp.status_code == 200


async def test_update(client: AsyncClient):
    username = shortuuid.uuid()
    password = shortuuid.uuid()
    data = UserCreate(
        username=username,
        password=password,
    )
    resp = await client.patch("/users/1", json=data.model_dump())
    assert resp.status_code == 200


async def test_delete(client: AsyncClient):
    resp = await client.delete("/users/1")
    assert resp.status_code == 200
