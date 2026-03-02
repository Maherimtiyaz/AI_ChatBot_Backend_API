from fastapi import FastAPI
from app.api.routes import chat, auth, sessions

app = FastAPI(title="AI Chatbot API")

app.include_router(auth.router, prefix="/auth")
app.include_router(chat.router, prefix="/chat")
app.include_router(sessions.router, prefix="/sessions")

@app.get("/health")
async def health():
    return {"status": "ok"}