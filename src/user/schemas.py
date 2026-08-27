from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    id: UUID
    email: str
    username: str
    last_login: datetime | None = None