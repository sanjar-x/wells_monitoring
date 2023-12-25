from fastapi import Header, HTTPException, status
from app.services.crud.user_crud import get_user
from app.core.security import verify


async def current_user(authorization: str = Header(...)):
    token = authorization.split(" ")[1]
    user_id = await verify(token)
    user_data = await get_user(user_id)
    if user_data:    
        return user_data
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Avtorizatsiyadan qaydadan o'ting"
    )


async def current_user_status(authorization: str = Header(...)):
    token = authorization.split(" ")[1]
    user_id = await verify(token)
    user_data = await get_user(user_id)
    if user_data:    
        return await user_data.get_status()
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Avtorizatsiyadan qaydadan o'ting"
    )