import os
import logging
from dotenv import load_dotenv
from uuid import UUID, uuid4
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from src.entities.user import User
from . import schemas


""" Set Enviroment Variables """
load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", default="your-secret-key")
ALGORITHM = os.getenv("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", default=30))


""" Main """
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


""" Endpoint Functions """
def register_user(database: Session, register_user_request: schemas.RegisterUserRequest) -> None:
    try:
        user = User(
            id=uuid4(),
            email=register_user_request.email,
            username=register_user_request.username,
            password_hash=get_password_hash(register_user_request.password)
        )
        database.add(user)
        database.commit()
    except Exception as e:
        logging.error(f"Failed to register user: {register_user_request.email}. Error: {str(e)}")
        raise
