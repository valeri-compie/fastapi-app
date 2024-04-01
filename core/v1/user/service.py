from sqlalchemy import sql
from sqlalchemy.ext.asyncio import AsyncSession

from core.v1.user.model import User
from core.v1.user.model import UserCreate
from core.v1.user.model import UserUpdate


async def insert(db: AsyncSession, payload: UserCreate) -> User:
    user = User(**payload.orm_dump())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def select(db: AsyncSession, user_id: int) -> User | None:
    stmt = sql.select(User).where(User.id == user_id)
    return await db.scalar(stmt)


async def select_by_username(db: AsyncSession, username: str) -> User | None:
    stmt = sql.select(User).where(User.username == username)
    return await db.scalar(stmt)


async def update(db: AsyncSession, user: User, payload: UserUpdate) -> User:
    for k, v in payload.orm_dump().items():
        user.__setattr__(k, v)
    await db.commit()
    await db.refresh(user)
    return user


async def delete(db: AsyncSession, user: User) -> None:
    await db.delete(user)
    await db.commit()
