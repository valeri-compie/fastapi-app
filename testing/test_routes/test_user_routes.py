from httpx import AsyncClient

import shortuuid
from core.v1.user.model import UserCreate
from core.v1.user.model import UserDetail
from core.v1.auth.util import verify_hash


async def test_user_status(user_client: AsyncClient):
    resp = await user_client.get("/users/status")
    assert resp.status_code == 200


async def test_create_user_a(user_client: AsyncClient):
    username = shortuuid.uuid()
    password = shortuuid.uuid()
    data = UserCreate(
        username=username,
        password=password,
    )
    resp = await user_client.post("/users/", json=data.model_dump())
    assert resp.status_code == 201
    user = UserDetail(**resp.json())
    assert user.username == username
    assert verify_hash(password, user.password)


async def test_create_user_b(user_client: AsyncClient):
    username = shortuuid.uuid()
    password = shortuuid.uuid()
    data = UserCreate(
        username=username,
        password=password,
    )
    resp = await user_client.post("/users/", json=data.model_dump())
    assert resp.status_code == 201
    user = UserDetail(**resp.json())
    assert user.username == username
    assert verify_hash(password, user.password)


async def test_select_user(user_client: AsyncClient, user_id: int = 2):
    resp = await user_client.get(f"/users/{user_id}")
    assert resp.status_code == 200
    user = UserDetail(**resp.json())
    assert user.id == user_id


async def test_update_user(user_client: AsyncClient, user_id: int = 2):
    username = shortuuid.uuid()
    password = shortuuid.uuid()
    data = UserCreate(
        username=username,
        password=password,
    )
    resp = await user_client.patch(f"/users/{user_id}", json=data.model_dump())
    assert resp.status_code == 200
    user = UserDetail(**resp.json())
    assert user.id == user_id
    assert user.username == username
    assert verify_hash(password, user.password)


async def test_delete_user(user_client: AsyncClient, user_id: int = 2):
    resp = await user_client.delete(f"/users/{user_id}")
    assert resp.status_code == 200
    resp = await user_client.get(f"/users/{user_id}")
    assert resp.status_code == 404
