
from sqlalchemy import Column, Integer, String, DateTime, func
from database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    phone_no = Column(String(20), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    salt = Column(String(255), nullable=False)
    role = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    # DateTime fields
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(),
                        onupdate=func.now(), nullable=False)

