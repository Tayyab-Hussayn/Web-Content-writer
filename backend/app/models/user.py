from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=True) # Nullable for OAuth
    full_name = Column(String)
    avatar_url = Column(Text)
    auth_provider = Column(String, default="email") # email, google
    subscription_tier = Column(String, default="free")
    stripe_customer_id = Column(String, nullable=True)
    global_instructions = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)

    generations = relationship("Generation", back_populates="user")
    usage_logs = relationship("UsageLog", back_populates="user")
    sessions = relationship("Session", back_populates="user")
