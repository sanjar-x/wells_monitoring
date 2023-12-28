from typing import List
from sqlalchemy import delete
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

from app.core.database import get_session
from app.models.well_models import MessageModel
from app.schemas.message_schemas import MessageSchema

async def create_message(message_data: MessageSchema) -> MessageModel:
    async with get_session() as session:
        created_message = MessageModel(**message_data.model_dump())
        session.add(created_message)
        await session.commit()
        return created_message

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

