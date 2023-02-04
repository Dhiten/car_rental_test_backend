from pydantic import BaseModel

class Vehicle(BaseModel):
    plate: str
    brand: str
    model: str
    doors: int
    vehicle_type: str