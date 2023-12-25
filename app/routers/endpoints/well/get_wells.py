from fastapi import APIRouter
from app.services.crud.well_crud import get_wells
router = APIRouter()

@router.get("/wells/")
async def get_wells_endpoint():
    return await get_wells()
