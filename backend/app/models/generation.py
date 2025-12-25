from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

# Note: for Postgres we would use JSONB, but SQLite uses JSON type if we import from sqlite dialect or generic JSON
# To make it compatible with both (mostly), we can use a custom type or just generic JSON from sqlalchemy.types if available (SQLAlchemy 2.0 has JSON)
from sqlalchemy.types import JSON as GenericJSON

class Generation(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    page_type = Column(String)
    business_context = Column(GenericJSON)
    image_url = Column(Text) # Or path if stored locally
    analysis_result = Column(GenericJSON)
    generated_content = Column(GenericJSON)
    model_used = Column(String)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="generations")
