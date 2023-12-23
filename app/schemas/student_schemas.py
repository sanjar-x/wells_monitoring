from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, List, Any

class StudentSchema(BaseModel):
    name: str
    surname: str
    phone_number: str
    email: str
    password_hash: str
    image: str