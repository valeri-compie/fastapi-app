from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

from core.v1.model import ORMModel
from core.v1.model import APIModel
from core.v1.auth.util import get_password_hash


class User(ORMModel):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)


class UserCreate(APIModel):
    username: str
    password: str

    def orm_dump(self):
        dump = self.model_dump()
        if "password" in dump.keys():
            pwd = dump["password"]
            hashed = get_password_hash(pwd)
            dump["password"] = hashed
        return dump


class UserDetail(APIModel):
    id: int
    username: str
    password: str


class UserUpdate(APIModel):
    username: str | None = None
    password: str | None = None

    def orm_dump(self):
        dump = self.model_dump(exclude_unset=True)
        if "password" in dump.keys():
            pwd = dump["password"]
            hashed = get_password_hash(pwd)
            dump["password"] = hashed
        return dump
