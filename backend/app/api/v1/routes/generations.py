from typing import Any
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.api.dependencies.auth import get_current_active_user
from app.models.user import User
from app.services.image_analysis import analysis_service
from app.services.content_generation import generation_service
from pydantic import Json

router = APIRouter()

@router.post("/analyze")
async def analyze_image(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    # 1. Read file
    contents = await file.read()
    
    # 2. Analyze
    analysis = await analysis_service.analyze_screenshot(contents)
    
    return analysis

@router.post("/generate")
async def generate_content(
    analysis_result: Json = Form(...),
    business_context: Json = Form(...),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    # 1. Generate
    content = await generation_service.generate_content(business_context, analysis_result)
    
    return content
