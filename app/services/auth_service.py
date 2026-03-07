from passlib.context import CryptContext
from app.core.config import settings
import jwt
import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")[:72]
    truncated = password_bytes.decode("utf-8", "ignore")
    return pwd_context.hash(truncated)


def verify_password(password: str, hashed: str) -> bool:
    password_bytes = password.encode("utf-8")[:72]
    truncated = password_bytes.decode("utf-8", "ignore")
    return pwd_context.verify(truncated, hashed)


def create_token(data: dict, expires_in_minutes: int = 60) -> str:
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