
from typing import List
from sqlalchemy import select
from app.core.database import get_session
from app.models.message_models import MessageModel
from app.schemas.messagge_schemas import MessageSchema

async def create_message(message_data: MessageSchema) -> MessageModel: 
    async with get_session() as session:
        created_message = MessageModel(**message_data.model_dump())
        session.add(created_message)
        await session.commit()
    return created_message

async def get_messages() -> List[MessageModel]:
    async with get_session() as session:
        result = await session.execute(select(MessageModel))
        messages = result.scalars().all()
        return messages
