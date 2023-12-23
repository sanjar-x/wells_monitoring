from sqlalchemy import Column, Integer, String
from app.core.database import Base
from uuid import uuid4

class StudentModel(Base):
    
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(String, unique=True, default=str(uuid4())[:8])
    name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    phone_number = Column(String, unique=True, nullable=True)
    email = Column(String, unique=True, nullable=True)
    password_hash = Column(String)
    image = Column(String)
