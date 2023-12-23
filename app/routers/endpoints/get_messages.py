from fastapi import APIRouter, status
from app.services.crud.message_crud import get_messages

router = APIRouter()

@router.get("/messages", status_code=status.HTTP_200_OK)
async def get_messages_():
    messages_data = await get_messages()
    return messages_data
