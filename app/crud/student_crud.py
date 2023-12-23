from app.core.database import get_session
from app.models.student_models import StudentModel
from app.schemas.student_schemas import StudentSchema

async def create_student(student_data: StudentSchema) -> StudentModel: 
	async with get_session() as session:
		created_student = StudentModel(**student_data.model_dump())
		session.add(created_student)
	return created_student
