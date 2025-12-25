from sqlalchemy.ext.asyncio import AsyncEngine
from app.db.base import Base
from app.models import User, Generation, UsageLog, Session  # Import all models

async def init_db(engine: AsyncEngine) -> None:
    """Initialize database tables"""
    async with engine.begin() as conn:
        # Create all tables
        await conn.run_sync(Base.metadata.create_all)
