from typing import Annotated
from fastapi import APIRouter, Request, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from ..rate_limiter import limiter
from ..database import DatabaseSession
from . import schemas
from . import service


router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
@limiter.limit("5/hour")
async def register_user(request: Request, # For the rate limiter to work.
                        database: DatabaseSession,
                        register_user_request: schemas.RegisterUserRequest):
    service.register_user(database, register_user_request)


@router.post("/token", response_model=schemas.Token)
@limiter.limit("1/minute")
async def login_for_access_token(request: Request, # For the rate limiter to work.
                                 # Includes things like username and password.
                                 form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 database: DatabaseSession):
    """ Get access token from username and password. """
    return service.login_for_access_token(form_data, database)
