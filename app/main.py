from fastapi import FastAPI
from app.api.routes import chat, auth, sessions


app = FastAPI(title="AI Chatbot API")


async def global_exception_handler(request, exc):
    return {"detail": str(exc)}


# Include routers
app.add_exception_handler(Exception, global_exception_handler)

app.include_router(auth.router, prefix="/auth")
app.include_router(chat.router, prefix="/chat")
app.include_router(sessions.router, prefix="/sessions")

@app.get("/health")
async def health():
    return {"status": "ok"}