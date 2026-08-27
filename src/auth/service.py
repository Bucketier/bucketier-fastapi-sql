import os
import logging
import jwt
from dotenv import load_dotenv
from uuid import UUID, uuid4
from datetime import datetime, timedelta, timezone
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from typing import Annotated
from src.entities.user import User
from src.exceptions import AuthenticationError
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
def register_user(database: Session, register_user_request: schemas.RegisterUserRequest):
    try:
        user = User(
            id=uuid4(),
            email=register_user_request.email,
            username=register_user_request.username,
            hashed_password=get_password_hash(register_user_request.password)
        )
        
        database.add(user)
        database.commit()
    except Exception as e:
        logging.error(f"Failed to register user: {register_user_request.email}. Error: {str(e)}")
        raise


def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                           database: Session) -> schemas.Token:
    user = authenticate_user(form_data.username, form_data.password, database)
    if not user: raise AuthenticationError()

    token = create_access_token(user.email, user.id, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return schemas.Token(access_token=token, token_type='bearer')


""" Helper Functions """
def get_password_hash(password: str) -> str:
    return bcrypt_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt_context.verify(plain_password, hashed_password)


def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]) -> schemas.TokenData:
    return verify_token(token)


def authenticate_user(email: str, password: str, db: Session) -> User | bool:
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        logging.warning(f"Failed authentication attempt for email: {email}")
        return False
    return user


def create_access_token(email: str, user_id: UUID, expires_delta: timedelta) -> str:
    encode = {
        'sub': email,
        'id': str(user_id),
        'exp': datetime.now(timezone.utc) + expires_delta
    }
    return jwt.encode(encode, JWT_SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str) -> schemas.TokenData:
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get('id')
        return schemas.TokenData(user_id=user_id)
    except jwt.PyJWTError as e:
        logging.warning(f"Token verification failed: {str(e)}")
        raise AuthenticationError()


""" Types """
CurrentUser = Annotated[schemas.TokenData, Depends(get_current_user)]