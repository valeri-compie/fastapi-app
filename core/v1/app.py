from contextlib import asynccontextmanager
from fastapi import FastAPI

from core.v1.config import config
from core.v1.database.service import create_default_user
from core.v1.database.service import create_tables
from core.v1.database.service import delete_tables
from core.v1.auth.router import router as auth_router
from core.v1.user.router import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    if config.IS_TESTING:
        await delete_tables()
        await create_tables()
    await create_default_user()
    yield
    if config.IS_TESTING:
        await delete_tables()


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/users")
