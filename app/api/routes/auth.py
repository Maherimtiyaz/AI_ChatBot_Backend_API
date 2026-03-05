from fastapi import APIRouter, HTTPException
from app.services.auth_service import hash_password, verify_password, create_token
from app.db.mongodb import users_collection

router = APIRouter()

@router.post("/signup")
async def signup(data: dict):
    existing = await users_collection.find_one({"email": data["email"]})
    if existing:
        raise HTTPException(status_code=400, detail="User exists")
    
    hashed = hash_password(data["password"])

    user = {
        "email": data["email"],
        "password_hash": hashed
    }

    await users_collection.inset_one(user)

    return {"message": "User created"}

@router.post("/login")
async def login(data: dict):
    user = await users_collection.find_one({"email": data["email"]})

    if not user or not verify_password(data["password"], user["password_hash"]):
        raise HTTPException(status_code=401, detail = "Invalid credentials")
    
    token = create_token({"id": str(user["_id"])})

    return {"access_token": token}
