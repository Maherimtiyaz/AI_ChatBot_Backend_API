from fastapi import APIRouter, HTTPException
from app.schemas.user import Usersignup, Userlogin
from app.services.auth_service import hash_password, verify_password, create_token
from app.db.mongodb import users_collection

router = APIRouter()

@router.post("/signup")
async def signup(data: dict):
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password required")

    existing = await users_collection.find_one({"email": email})
    if existing:
        raise HTTPException(status_code=400, detail="User exists")

    hashed = hash_password(password)

    user = {
        "email": email,
        "password_hash": hashed
    }

    await users_collection.insert_one(user)
    return {"message": "User created"}

@router.post("/login")
async def login(data: dict):
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password required")

    user = await users_collection.find_one({"email": email})

    if not user or not verify_password(password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"id": str(user["_id"])})

    return {"access_token": token}