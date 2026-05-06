# FastAPI Auth Learning Project

A simple authentication API built with FastAPI.

## Features
- User registration
- Login with JWT authentication
- Protected route (`/me`)
- Password hashing with bcrypt
- SQLite database

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- Passlib (bcrypt)
- JWT (python-jose)

## Setup

### 1. Clone repo
```bash
git clone <repo-url>
cd fastapi-auth

```

### 2. Create virtual environment
```bash 
python -m venv venv
venv\Scripts\activate

```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run server
```bash
uvicorn app.main:app --reload
```