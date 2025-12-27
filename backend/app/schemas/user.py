from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, Field
from datetime import datetime

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=16)  # 8-16 characters
    full_name: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDBBase(UserBase):
    id: Optional[int] = None
    email: EmailStr
    auth_provider: str
    subscription_tier: str
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

class User(UserInDBBase):
    pass
