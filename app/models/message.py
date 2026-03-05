from pydantic import BaseModel 
from datetime import datetime

class Message(BaseModel):
    session_id: str
    role: str
    content: str
    created_at: datetime = datetime.utcnow()