from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.auth import UserCreate, Token

router = APIRouter()

# NOTE: these are placeholders — we'll implement DB and JWT next
@router.post("/register", response_model=dict, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate):
    # In next sessions we'll:
    #  - hash password using passlib
    #  - save using SQLAlchemy session
    # For now, return a mock success
    return {"msg": "user registered (placeholder)", "username": user.username}

@router.post("/login", response_model=Token)
def login():
    # placeholder: real login will return JWT token
    return {"access_token": "fake-token", "token_type": "bearer"}
