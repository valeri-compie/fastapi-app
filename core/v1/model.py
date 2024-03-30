from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel


class ORMModel(DeclarativeBase): ...


class APIModel(BaseModel): ...
