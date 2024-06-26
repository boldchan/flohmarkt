from core.hashing import Hasher
from db.models.user import User
from schemas.user import UserCreate
from sqlalchemy.orm import Session


def create_new_user(user: UserCreate, db: Session):
    user = User(
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(email: str, db: Session):
    user_in_db = db.query(User).filter(User.email == email).first()
    return user_in_db
