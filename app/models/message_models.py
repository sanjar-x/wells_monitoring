from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from app.core.database import Base
from datetime import datetime
from uuid import uuid4

class MessageModel(Base):
    
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    T = Column(String, nullable=True)
    H = Column(String, nullable=True)
    A = Column(String, nullable=True)
    time = Column('time', DateTime, default=datetime.utcnow)
