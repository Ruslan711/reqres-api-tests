from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime


class UpdateUserRequest(BaseModel):
    name: Optional[str] = Field(min_length=2)
    job: Optional[str] = Field(min_length=2)

    @validator("name")
    def validate_name(cls, value):
        if value is not None and not value.strip():
            raise ValueError("короткое имя")
        return value

    @validator("job")
    def validate_job(cls, value):
        if value is not None and not value.strip():
            raise ValueError("короткое название работы")
        return value


class UpdateUserResponse(BaseModel):
    name: str
    job: str
    updatedAt: datetime
