import asyncio
from app.core.database import Base, engine



async def init_database():
    from app.models.student_models import StudentModel
    from app.models.message_models import MessageModel
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def main():
    await init_database()

if __name__ == "__main__":
    asyncio.run(main())