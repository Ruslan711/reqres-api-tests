from typing import List

from pydantic import BaseModel

from services.reqres_in.common.models.support import Support


class ResourceData(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


class SingleResourceResponse(BaseModel):
    data: ResourceData
    support: Support


class ResourcesListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[ResourceData]
    support: Support
