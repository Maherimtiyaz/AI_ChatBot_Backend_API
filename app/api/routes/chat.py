from fastapi import APIRouter, Depends, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import process_message
from app.core.security import get_current_user

router = APIRouter()

@router.post("/{session_id}", response_model=ChatResponse)
async def chat(session_id: str, req: ChatRequest, user=Depends(get_current_user)):
    try:
        response = await process_message(session_id, user["id"], req.message)
        return response
    except Exception:
        raise HTTPException(status_code=500, detail="Chat processing failed")