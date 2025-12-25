from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class UsageLog(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    action_type = Column(String) # generation, analysis
    model_used = Column(String)
    tokens_used = Column(Integer)
    
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="usage_logs")
