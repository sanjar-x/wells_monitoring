from typing import List
from sqlalchemy import select, delete
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

from app.core.database import get_session
from app.models.message_models import MessageModel
from app.schemas.messagge_schemas import MessageSchema


async def create_message(message_data: MessageSchema) -> MessageModel:
    async with get_session() as session:
        try:
            # Ручное преобразование данных из схемы в модель
            created_message = MessageModel(
                temperature=message_data.T,
                salinity=message_data.H,
                water_level=message_data.A
            )
            session.add(created_message)
            await session.commit() # type: ignore
            return created_message
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Message not saved to the server")

async def get_messages() -> List[MessageModel]:
    async with get_session() as session:
        result = await session.execute(select(MessageModel)) # type: ignore
        messages = result.scalars().all()
        return messages

async def delete_messages():
    try:
        async with get_session() as session:
            await session.execute(delete(MessageModel)) # type: ignore
            await session.commit() # type: ignore
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error deleting messages")

