from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, List, Any


class MessageSchema(BaseModel):
    message: str
    temperature: str
    salinity: str
    water_level: str
    number: str
