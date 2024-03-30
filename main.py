import uvicorn

from core.v1.app import app
from core.v1.config import config


if __name__ == "__main__":
    # T1
    uvicorn.run(app=app, host=config.UVICORN_HOST, port=config.UVICORN_PORT)
