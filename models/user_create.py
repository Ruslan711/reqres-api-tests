from pydantic import BaseModel, Field, validator
from datetime import datetime


class UserRequest(BaseModel):
    name: str = Field(min_length=2)
    job: str = Field(min_length=2)

    @validator("name")
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("короткое имя")
        return value

    @validator("job")
    def validate_job(cls, value):
        if not value.strip():
            raise ValueError("короткое название работыы")
        return value


class UserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: datetime
