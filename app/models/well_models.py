import uuid
from datetime import datetime, timezone
from time import time
from sqlalchemy import Column, String, DateTime, Boolean
from app.core.database import Base


class WelleModel(Base):
    __tablename__ = "wells"

    well_id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False,
    )
    name = Column(String, nullable=True)
    number = Column(String, unique=True)
    address = Column(String, nullable=True)
    latitude = Column(String, nullable=True)
    longitude = Column(String, nullable=True)
    status = Column(Boolean, default=True)
    created_time = Column("time", DateTime, default=datetime.now(timezone.utc))


class MessageModel(Base):
    __tablename__ = "messages"

    message_id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False,
    )
    temperature = Column(String, nullable=True)
    salinity = Column(String, nullable=True)
    water_level = Column(String, nullable=True)
    number = Column(String, nullable=True)
    time = Column("time", DateTime, default=datetime.now(timezone.utc))
