from sqlalchemy.ext.asyncio import create_async_engine

from core.v1.config import config

engine = create_async_engine(url=config.POSTGRES_DSN, echo=True)
