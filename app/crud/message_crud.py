from typing import List
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.core.database import get_session
from app.models.message_models import MessageModel
from app.schemas.messagge_schemas import MessageSchema
from fastapi import HTTPException

async def create_message(message_data: MessageSchema) -> MessageModel: 
    try:
        async with get_session() as session:
            created_message = MessageModel(**message_data.model_dump())
            session.add(created_message)
            await session.commit()
        return created_message
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Habar serverga saqlanmadi")

async def get_messages() -> List[MessageModel]:
    async with get_session() as session:
        result = await session.execute(select(MessageModel))
        messages = result.scalars().all()
        return messages

async def delete_messages():
    async with get_session() as session:

        messages = await session.execute(select(MessageModel))
        
        for message in messages.scalars().all():
            session.delete(message)

        await session.commit()

