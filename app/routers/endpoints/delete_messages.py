from fastapi import APIRouter, Depends, HTTPException, status
from app.crud.message_crud import delete_messages

router = APIRouter()

@router.delete("/messages")
async def delete_messages_():
    await delete_messages()
    return {"message": "Habarlar o'chirildi"}