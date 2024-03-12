import asyncio
from app.core.database import Base, engine


async def init_database():
    from app.models.models import UserModel
    from app.models.models import WellsModel, MessageModel
    from app.models.models import StatementModel

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def main():
    await init_database()


if __name__ == "__main__":
    asyncio.run(main())
