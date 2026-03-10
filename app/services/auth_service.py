from passlib.context import CryptContext
from app.core.config import settings
import jwt
import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)


def create_token(data: dict, expires_in_minutes: int = 60):
    payload = data.copy()

    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(
        minutes=expires_in_minutes
    )

    token = jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM
    )

    return token