from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.core.database import engine
from app.models.models import Base

settings_router = APIRouter()


@settings_router.get("/database/reset")
async def reset_database():
    async with engine.begin() as connection:

        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
        return JSONResponse(content={"database": "reseted"})
