from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./app/core/database.db"
engine = create_async_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession)  # type: ignore
Base = declarative_base()


@asynccontextmanager
async def get_session():
    session = SessionLocal()
    try:
        yield session
    except Exception as e:
        await session.rollback()  # type: ignore
        raise
    finally:
        await session.close()  # type: ignore
