from pydantic import BaseModel, HttpUrl


class FacilityURL(BaseModel):
    url: HttpUrl


class FacilityData(BaseModel):
    facility_id: str
    name: str
    facility_type: str
    active: bool
    alias: list
