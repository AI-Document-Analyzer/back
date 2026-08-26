from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.schemas.auth import SignupRequest


def create_user(db: Session, signup_data: SignupRequest) -> User:
    existing_user = db.query(User).filter(User.email == signup_data.email).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    user = User(
        email=signup_data.email,
        name=signup_data.name,
        password_hash=hash_password(signup_data.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user