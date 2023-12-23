from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base

class MessageModel(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    temperature = Column(String, nullable=True)
    salinity = Column(String, nullable=True)
    water_level = Column(String, nullable=True)
    time = Column('time', DateTime, default=datetime.utcnow)
