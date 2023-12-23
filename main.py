from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from uvicorn import run

from app.routers.endpoints.create_message import router as create_message_router
from app.routers.endpoints.get_messages import router as get_messages_router
HTTP_PORT = 8001

app = FastAPI(
    title="WEB Algoritm API",
    description="API-документация для веб-платформы учебного центра Algoritm",
    version="0.0.1",
)


app.include_router(router=create_message_router, tags=["message"])
app.include_router(router=get_messages_router, tags=["message"])


if __name__ == '__main__':
    run(app, host="0.0.0.0", port=HTTP_PORT, access_log=False)