# AI Chatbot Backend (FastAPI + MongoDB)

## Overview

This project implements a backend service for an AI-powered chatbot system. It allows users to authenticate, create chat sessions, interact with an AI assistant, and store conversation history.

The backend is built using FastAPI and MongoDB, following a modular and scalable architecture.

### Key Features

- User authentication using JWT
- Chat session management
- AI-powered chat responses
- Persistent message storage
- Modular and scalable backend design
- Interactive API documentation with Swagger

---

## Tech Stack

- **Backend Framework:** FastAPI  
- **Database:** MongoDB  
- **Async Driver:** Motor  
- **Authentication:** JWT (JSON Web Tokens)  
- **Password Hashing:** Passlib (bcrypt)  
- **Validation:** Pydantic  
- **AI Integration:** Google Gemini API (optional)  
- **Documentation:** Swagger / OpenAPI  

---

## Architecture

    Client (Swagger / Frontend)
    │
    ▼
    API Routes (FastAPI)
    │
    ▼
    Service Layer (Business Logic)
    │
    ▼
    Database Layer (MongoDB)

### Layers

- **API Layer:** Handles HTTP requests and responses  
- **Service Layer:** Contains business logic  
- **Database Layer:** Manages data persistence  
- **Schemas:** Validate request and response data  
- **Core:** Handles configuration and security  
- **Middleware:** Logging and error handling  

---

## Project Structure

    app/
    ├── main.py
    ├── core/
    │   ├── config.py
    │   ├── security.py
    │
    ├── api/
    │   └── routes/
    │       ├── auth.py
    │       ├── chat.py
    │       └── sessions.py
    │
    ├── models/
    │   ├── user.py
    │   ├── session.py
    │   └── message.py
    │
    ├── schemas/
    │   ├── user.py
    │   └── chat.py
    │
    ├── services/
    │   ├── auth_service.py
    │   ├── chat_service.py
    │   └── llm_service.py
    │
    ├── db/
    │   └── mongodb.py
    │
    ├── middleware/
    │   ├── logging.py
    │   └── error_handler.py

---

## File-Level Explanation

### main.py
Initializes FastAPI application, registers routes, and loads middleware.

### core/config.py
Manages environment variables such as database connection, JWT secrets, and API keys.

### core/security.py
Handles JWT authentication and extracts user information from tokens.

### api/routes/auth.py
Provides authentication endpoints:
- POST /auth/signup
- POST /auth/login

### api/routes/sessions.py
Handles chat session creation:
- POST /sessions

### api/routes/chat.py
Handles chatbot interaction:
- POST /chat/{session_id}
- GET /sessions/{session_id}

### models/
Defines data structures for users, sessions, and messages.

### schemas/
Defines request and response validation using Pydantic.

### services/
Contains business logic:
- auth_service.py → authentication logic  
- chat_service.py → chat handling  
- llm_service.py → AI response generation  

### db/mongodb.py
Initializes MongoDB connection and collections.

### middleware/
Handles logging and error management.

---

## API Documentation

Swagger UI is available at:

    http://127.0.0.1:8000/docs

It provides:

- Interactive API testing
- Request/response schemas
- Authorization support

---

## API Endpoints

### Authentication

#### Signup

POST /auth/signup

Request:

    {
      "email": "user@example.com",
      "password": "password123"
    }

#### Login

POST /auth/login

Response:

    {
      "access_token": "JWT_TOKEN"
    }

---

### Sessions

#### Create Session

POST /sessions

Response:

    {
      "session_id": "session_id"
    }

---

### Chat

#### Send Message

POST /chat/{session_id}

Request:

    {
      "message": "Hello AI"
    }

Response:

    {
      "reply": "AI response"
    }

---

#### Get Chat History

GET /sessions/{session_id}

Response:

    {
      "session_id": "...",
      "messages": [...]
    }

---

## Database Schema

### Users Collection

    {
      "_id": ObjectId,
      "email": "string",
      "password_hash": "string"
    }

### Sessions Collection

    {
      "_id": ObjectId,
      "user_id": "string",
      "created_at": "timestamp"
    }

### Messages Collection

    {
      "_id": ObjectId,
      "session_id": "string",
      "role": "user | assistant",
      "content": "string",
      "timestamp": "timestamp"
    }

---

## Setup Instructions

### 1. Clone Repository

    git clone <repository-url>
    cd ai-chatbot-backend

### 2. Create Virtual Environment

    python -m venv venv

Activate (Windows):

    venv\Scripts\activate

---

### 3. Install Dependencies

    pip install -r requirements.txt

---

### 4. Environment Variables

Create a `.env` file:

    MONGO_URL=mongodb://localhost:27017
    DATABASE_NAME=ai_chatbot_db

    JWT_SECRET=your_secure_secret
    JWT_ALGORITHM=HS256

    LLM_PROVIDER=mock
    GEMINI_API_KEY=

---

### 5. Run Server

    uvicorn app.main:app --reload

Visit:

    http://127.0.0.1:8000/docs

---

## Assumptions

- Each user can create multiple chat sessions
- Each session represents one conversation
- Messages are stored separately and linked via session_id
- JWT is used for authentication
- Passwords are hashed using bcrypt
- MongoDB is used for flexible schema handling
- AI provider can be switched between mock and real

---

## Advanced Feature

### Context-Aware Chat Memory

Example:

    User: What is Python?
    AI: Python is a programming language.

    User: Who created it?

With context:

    AI: Python was created by Guido van Rossum.

---

## Future Improvements

- Streaming responses
- Rate limiting
- Chat summarization
- Multi-user chat support
- AI moderation system

---

## Conclusion

This project demonstrates a scalable and modular backend system for AI-powered chat applications. It follows best practices in API design, authentication, and database handling, making it suitable for real-world applications and further extension.