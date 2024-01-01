import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Boolean
from app.core.database import Base

class StatementModel(Base):
    __tablename__ = "statements"

    statement_id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False,
    )
    statement = Column(String, nullable=True)
    number = Column(String, nullable=True)
    time = Column("time", DateTime, default=datetime.now(timezone.utc))