from typing import List
from pydantic import BaseModel, HttpUrl
from models.user import User


class Support(BaseModel):
    url: HttpUrl
    text: str


class PaginationResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[User]
    support: Support