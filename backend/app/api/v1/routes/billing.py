from fastapi import APIRouter

router = APIRouter()

@router.post("/webhook")
async def stripe_webhook():
    return {"status": "success"}
