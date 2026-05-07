from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from services.reqres_in.common.models.support import Support

class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class SingleUserResponse(BaseModel):
    data: UserData
    support: Support


class UsersListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[UserData]
    support: Support


class CreateUserRequest(BaseModel):
    name: str
    job: str


class CreateUserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: datetime


class UpdateUserRequest(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2)
    job: Optional[str] = Field(default=None, min_length=2)


class UpdateUserResponse(BaseModel):
    name: Optional[str] = None
    job: Optional[str] = None
    updatedAt: str