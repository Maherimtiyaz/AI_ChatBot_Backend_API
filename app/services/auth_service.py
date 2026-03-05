from passlib.context import CryptContext
from jose import JWTError
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET = "your_secret_key"
ALGORITHM = "HS256"

# Hash a password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verify a password
def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)

# Create a JWT token
def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(hours=24)
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)