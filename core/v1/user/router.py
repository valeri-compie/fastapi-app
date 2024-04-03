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
from core.v1.auth.require import active_jwt_subject
from core.v1.user import service


router = APIRouter()


@router.get("/status", response_class=Response, tags=["User"])
async def status(
    active_user: UserDetail = Depends(active_jwt_subject),
    db: AsyncSession = Depends(db_session),
):
    return Response(status_code=200)


@router.post("/", response_model=UserDetail, status_code=201, tags=["User"])
async def create_user(
    payload: UserCreate,
    active_user: UserDetail = Depends(active_jwt_subject),
    db: AsyncSession = Depends(db_session),
):
    return await service.create(db=db, payload=payload)


@router.get("/me", response_model=UserDetail, tags=["User"])
async def read_users_me(
    active_user: UserDetail = Depends(active_jwt_subject),
):
    return active_user


@router.get("/{user_id}", response_model=UserDetail, tags=["User"])
async def select_user(
    target_user: User = Depends(target_user),
    active_user: UserDetail = Depends(active_jwt_subject),
):
    return target_user


@router.patch("/{user_id}", response_model=UserDetail, tags=["User"])
async def update_user(
    payload: UserUpdate,
    target_user: User = Depends(target_user),
    active_user: UserDetail = Depends(active_jwt_subject),
    db: AsyncSession = Depends(db_session),
):
    return await service.update(db=db, user=target_user, payload=payload)


@router.delete("/{user_id}", response_class=Response, tags=["User"])
async def delete_user(
    target_user: User = Depends(target_user),
    db: AsyncSession = Depends(db_session),
    active_user: UserDetail = Depends(active_jwt_subject),
):
    await service.delete(db=db, user=target_user)
    return Response(status_code=200)
