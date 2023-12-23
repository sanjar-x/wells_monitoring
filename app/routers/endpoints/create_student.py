from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.student_schemas import StudentSchema
from app.crud.student_crud import create_student

router = APIRouter()

@router.post("/create")
async def create_employee_(student_data: StudentSchema):
    created_student_data = await create_student(student_data)
    return {"data": created_student_data}
