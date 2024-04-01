from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import Security

from core.v1.database.require import db_session
from core.v1.user.model import User
from core.v1.user.model import UserCreate
from core.v1.user.model import UserDetail
from core.v1.user.model import UserUpdate
from core.v1.user.service import insert
from core.v1.user.service import update
from core.v1.user.service import delete
from core.v1.user.require import user_in_path
from core.v1.auth.require import get_current_active_user
from core.v1.auth.require import authorized_user


router = APIRouter()


@router.get("/status", response_class=Response)
async def status(
    db: AsyncSession = Depends(db_session),
):
    return Response(status_code=200)


@router.post("/", response_model=UserDetail, status_code=201)
async def create_user(
    payload: UserCreate,
    db: AsyncSession = Depends(db_session),
    current_user: UserDetail = Security(get_current_active_user, scopes=["user-create"]),
):
    return await insert(db=db, payload=payload)


@router.get("/{user_id}", response_model=UserDetail)
async def select_user(
    target_user: User = Depends(user_in_path),
    current_user: UserDetail = Security(get_current_active_user, scopes=["user-select"]),
):
    return target_user


@router.patch("/{user_id}", response_model=UserDetail)
async def update_user(
    payload: UserUpdate,
    target_user: User = Depends(user_in_path),
    db: AsyncSession = Depends(db_session),
    current_user: UserDetail = Security(get_current_active_user, scopes=["user-update"]),
):
    return await update(db=db, user=target_user, payload=payload)


@router.delete("/{user_id}", response_class=Response)
async def delete_user(
    target_user: User = Depends(user_in_path),
    db: AsyncSession = Depends(db_session),
    current_user: UserDetail = Security(get_current_active_user, scopes=["user-delete"]),
):
    await delete(db=db, user=target_user)
    return Response(status_code=200)


@router.get("/me/", response_model=UserDetail)
async def read_users_me(
    current_user: UserDetail = Depends(get_current_active_user),
):
    return current_user
