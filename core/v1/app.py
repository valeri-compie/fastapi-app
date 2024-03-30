from contextlib import asynccontextmanager
from fastapi import FastAPI

from core.v1.user.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router, prefix="/users")
