from httpx import AsyncClient

import shortuuid
from core.v1.user.model import UserCreate


async def test_create_user_a(client: AsyncClient):
    username = shortuuid.uuid()
    password = shortuuid.uuid()
    data = UserCreate(
        username=username,
        password=password,
    )
    resp = await client.post("/users/", json=data.model_dump())
    assert resp.status_code == 201


async def test_create_user_b(client: AsyncClient):
    username = shortuuid.uuid()
    password = shortuuid.uuid()
    data = UserCreate(
        username=username,
        password=password,
    )
    resp = await client.post("/users/", json=data.model_dump())
    assert resp.status_code == 201


async def test_select_user(client: AsyncClient):
    resp = await client.get("/users/2")
    assert resp.status_code == 200


async def test_update_user(client: AsyncClient):
    username = shortuuid.uuid()
    password = shortuuid.uuid()
    data = UserCreate(
        username=username,
        password=password,
    )
    resp = await client.patch("/users/2", json=data.model_dump())
    assert resp.status_code == 200


async def test_delete_user(client: AsyncClient):
    resp = await client.delete("/users/2")
    assert resp.status_code == 200
