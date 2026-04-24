from typing import List

from pydantic import BaseModel, HttpUrl


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: HttpUrl


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
