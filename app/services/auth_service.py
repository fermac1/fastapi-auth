from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password, verify_password
from app.core.logger import logger

def create_user(db: Session, email: str, password: str):
    try:
        logger.info(f"REGISTER attempt | email={email}")

        user = User(
            email=email,
            password=hash_password(password)
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        logger.info(f"USER CREATED | id={user.id} | email={user.email}")
        return user

    except Exception as e:
        logger.exception("REGISTER FAILED")
        raise

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        return None
    return user