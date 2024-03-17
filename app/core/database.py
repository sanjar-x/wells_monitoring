from contextlib import asynccontextmanager
from logging import error
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio.engine import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./app/core/database.db"
engine = create_async_engine(DATABASE_URL)
sessionmaker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=True,
    twophase=False,
)
# type: ignore
Base = declarative_base()


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with sessionmaker() as session:
        try:
            yield session
        except:
            await session.rollback()
            error(f"Session rollback due to error")
            raise
        finally:
            await session.close()
