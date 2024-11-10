from pydantic import BaseModel


class AddLocationData(BaseModel):
    type: str
    data: str
    class Config:
        from_attributes = True


class LocationData(AddLocationData):
    id: int