from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

from core.v1.model import ORMModel
from core.v1.model import APIModel


class User(ORMModel):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)


class UserCreate(APIModel):
    username: str
    password: str

    def orm_dump(self):
        return self.model_dump()


class UserDetail(APIModel):
    id: int
    username: str
    password: str


class UserUpdate(APIModel):
    username: str | None = None
    password: str | None = None

    def orm_dump(self):
        return self.model_dump(exclude_unset=True)
