from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.orm import relationship
from .base import Base

class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(TIMESTAMP, default=func.now())
    last_login = Column(TIMESTAMP)

    # Relationships
    test_sessions = relationship("TestSession", back_populates="account")
    user_contexts = relationship("UserContext", back_populates="account")