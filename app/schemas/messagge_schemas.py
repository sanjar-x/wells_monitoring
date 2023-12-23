from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, List, Any

class MessageSchema(BaseModel):
    T: str
    H: str
    A: str
