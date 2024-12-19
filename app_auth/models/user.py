import uuid
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app_auth.databases.database import Base, engine

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    is_disabled = Column(Boolean, name='disable')
    guid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True)
    hashed_password = Column(String)

    __table_args__ = (
        {'extend_existing': True},
    )

Base.metadata.create_all(bind=engine)