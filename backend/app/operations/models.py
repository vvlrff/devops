from datetime import datetime

from fastapi_users_db_sqlalchemy.generics import GUID
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, Boolean, Float

from app.database import metadata

post = Table(
    "file",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("text", String),
    Column("owner", GUID, ForeignKey('user.id'))
)
