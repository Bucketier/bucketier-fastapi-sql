from fastapi import APIRouter
from src.auth.service import CurrentUser
from src.database import DatabaseSession
from . import schemas
from . import service


router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get("/me", response_model=schemas.UserResponse)
def get_current_user(current_user: CurrentUser, db: DatabaseSession):
    return service.get_user_by_id(db, current_user.get_uuid())