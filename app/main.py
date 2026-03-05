from fastapi import FastAPI
from app.api.routes import chat, auth, sessions
from app.middleware.logging import log_requests
from app.middleware.error_handler import global_exception_handler

app = FastAPI(title="AI Chatbot API")


async def global_exception_handler(request, exc):
    return {"detail": str(exc)}


async def log_requests(request, call_next):
    response = await call_next(request)
    return response

# Register middleware
app.middleware("http")(log_requests)

app.include_router(auth.router, prefix="/auth")
app.include_router(chat.router, prefix="/chat")
app.include_router(sessions.router, prefix="/sessions")

# Register global error handler
app.add_exception_handler(Exception, global_exception_handler)

@app.get("/health")
async def health():
    return {"status": "ok"}