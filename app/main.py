from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.responses import Response
from app.api.routes import chat, auth, sessions
from app.middleware.logging import log_requests
from app.middleware.error_handler import global_exception_handler

app = FastAPI(title="AI Chatbot API")


# Middleware for logging requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    return response  # just return response, do NOT call it

# Global exception handler must return JSONResponse
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)}
    )

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