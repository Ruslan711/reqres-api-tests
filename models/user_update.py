from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator

class UpdateUserRequest(BaseModel):

    name: Optional[str] = Field(min_length=2)
    job: Optional[str] = Field(min_length=2)

    @field_validator("name", "job")
    @classmethod
    def strip_and_validate(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return value
        stripped = value.strip()
        if not stripped:
            raise ValueError("field cannot be empty")
        return stripped


class UpdateUserResponse(BaseModel):
    name: str
    job: str
    updatedAt: datetime
