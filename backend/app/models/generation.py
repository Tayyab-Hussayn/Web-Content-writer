from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.types import JSON as GenericJSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

# Use JSONB for PostgreSQL (falls back to JSON for other databases)

class Generation(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    page_type = Column(String)
    business_context = Column(JSONB)
    image_url = Column(Text) # Or path if stored locally
    analysis_result = Column(JSONB)
    generated_content = Column(JSONB)
    model_used = Column(String)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="generations")
