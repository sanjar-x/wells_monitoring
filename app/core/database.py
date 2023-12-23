# import logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./app/core/database.db"
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

@asynccontextmanager
async def get_session():
    session = SessionLocal()
    try:
        yield session
    except Exception as e:
        # logger.error(f"Session rollback because of error: {e}")
        await session.rollback()
        raise
    finally:
        await session.close()