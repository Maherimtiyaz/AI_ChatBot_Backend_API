from pydantic import BaseModel
from datetime import datetime


class Session(BaseModel):
    user_id: str
    created_at: datetime = datetime.utcnow()
    last_active: datetime = datetime.utcnow()