from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class UpdateUserRequest(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2)
    job: Optional[str] = Field(default=None, min_length=2)

    @field_validator("name", "job")
    @classmethod
    def strip_and_validate(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return value

        value = value.strip()
        if not value:
            raise ValueError("поле не может быть пустым")

        return value


class UpdateUserResponse(BaseModel):
    name: str
    job: str
    updatedAt: datetime
