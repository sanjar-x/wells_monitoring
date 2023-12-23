from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.messagge_schemas import MessageSchema
from app.crud.message_crud import create_message

router = APIRouter()

@router.post("/message", status_code=status.HTTP_201_CREATED)
async def create_message_(message_data: MessageSchema):
    await create_message(message_data)
    return {"message": "Habar qabul qilindi"}