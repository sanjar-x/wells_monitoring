from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.messagge_schemas import MessageSchema
from app.crud.message_crud import create_message

router = APIRouter()

@router.post("/message")
async def create_message_(message_data: MessageSchema):
    created_message = await create_message(message_data)
    return created_message
