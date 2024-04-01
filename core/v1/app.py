from contextlib import asynccontextmanager
from fastapi import FastAPI

from core.v1.auth import router as auth_router
from core.v1.user.router import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router, prefix="/token")
app.include_router(user_router, prefix="/users")
