import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, Boolean, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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


class WellsModel(Base):
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
