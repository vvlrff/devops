from datetime import datetime
from uuid import uuid4

from fastapi_users_db_sqlalchemy.generics import GUID
from fastapi_users_db_sqlalchemy import UUID_ID, SQLAlchemyBaseUserTableUUID
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean
from sqlalchemy.dialects.postgresql import ARRAY

from app.database import Base, metadata

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    id: UUID_ID = Column(GUID, primary_key=True, default=uuid4)
    email: str = Column(String(length=320), unique=True, index=True, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id))
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)