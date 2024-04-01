from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response

from core.v1.database.require import db_session
from core.v1.user.model import User
from core.v1.user.model import UserCreate
from core.v1.user.model import UserDetail
from core.v1.user.model import UserUpdate
from core.v1.user.require import target_user
from core.v1.auth.require import active_user
from core.v1.user import service


router = APIRouter()


@router.get("/status", response_class=Response)
async def status(
    active_user: UserDetail = Depends(active_user),
    db: AsyncSession = Depends(db_session),
):
    return Response(status_code=200)


@router.post("/", response_model=UserDetail, status_code=201)
async def create_user(
    payload: UserCreate,
    active_user: UserDetail = Depends(active_user),
    db: AsyncSession = Depends(db_session),
):
    return await service.create(db=db, payload=payload)


@router.get("/me", response_model=UserDetail)
async def read_users_me(
    active_user: UserDetail = Depends(active_user),
):
    return active_user


@router.get("/{user_id}", response_model=UserDetail)
async def select_user(
    target_user: User = Depends(target_user),
    active_user: UserDetail = Depends(active_user),
):
    return target_user


@router.patch("/{user_id}", response_model=UserDetail)
async def update_user(
    payload: UserUpdate,
    target_user: User = Depends(target_user),
    active_user: UserDetail = Depends(active_user),
    db: AsyncSession = Depends(db_session),
):
    return await service.update(db=db, user=target_user, payload=payload)


@router.delete("/{user_id}", response_class=Response)
async def delete_user(
    target_user: User = Depends(target_user),
    db: AsyncSession = Depends(db_session),
    active_user: UserDetail = Depends(active_user),
):
    await service.delete(db=db, user=target_user)
    return Response(status_code=200)
