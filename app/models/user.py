from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    email: EmailStr
    password_hash: str
    created_at: datetime = datetime.utcnow()