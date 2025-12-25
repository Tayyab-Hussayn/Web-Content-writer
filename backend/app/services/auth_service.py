from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash, verify_password, create_access_token, create_refresh_token
from app.core.config import settings

async def authenticate_user(db: AsyncSession, email: str, password: str):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()
    if not user:
        return False
    if not user.password_hash: # OAuth user trying to login with password
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user

async def create_user(db: AsyncSession, user_in: UserCreate):
    result = await db.execute(select(User).where(User.email == user_in.email))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    
    db_user = User(
        email=user_in.email,
        password_hash=get_password_hash(user_in.password),
        full_name=user_in.full_name,
        auth_provider="email",
        subscription_tier="free"
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
