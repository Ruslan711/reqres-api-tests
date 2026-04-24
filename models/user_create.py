from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserRequest(BaseModel):
    name: str
    job: str


class UserResponse(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    job: Optional[str] = None
    createdAt: Optional[datetime] = None