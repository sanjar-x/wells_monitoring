import uuid
from sqlalchemy import Column, String, Boolean
from app.core.database import Base

class UserModel(Base):
    __tablename__ = "users"

    user_id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False,
    )
    username = Column(String, unique=True)
    password_hash = Column(String)
    name = Column(String)
    surname = Column(String)
    is_superuser = Column(Boolean, default=False)

    async def get_status(self):
        return self.is_superuser

    async def set_status(self, is_superuser: bool):
        self.is_superuser = is_superuser