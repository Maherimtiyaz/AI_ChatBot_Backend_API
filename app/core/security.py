from jose import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer

SECRET = "secret"

security = HTTPBearer()

def get_current_user(token=Depends(security)):
    try:
        payload = jwt.decode(token.credentials, SECRET, algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")