from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.db.mongodb import sessions_collection

router = APIRouter()

@router.post("/")
async def create_session(user=Depends(get_current_user)):
    session = {
        "user_id": user["id"]
    }
    result = await sessions_collection.insert_one(session)
    return {"session_id": str(result.inserted_id)}


@router.get("/")
async def get_sessions(user=Depends(get_current_user)):
    sessions = await sessions_collection.find(
        {"user_id": user["id"]}
        
    ).to_list(100)
    
    return sessions