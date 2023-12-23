from fastapi import APIRouter, Depends, HTTPException, status
from app.crud.message_crud import get_messages

router = APIRouter()

@router.get("/messages")
async def create_messages_():
    messeges_data = await get_messages()
    return messeges_data
