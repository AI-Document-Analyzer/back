from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.auth import SignupRequest, UserResponse
from app.service.user_service import create_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=UserResponse,
             status_code=status.HTTP_201_CREATED)
def signup(signup_data: SignupRequest, db: Session = Depends(get_db)):
    return create_user(db, signup_data)

