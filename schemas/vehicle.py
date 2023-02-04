from pydantic import BaseModel
from typing import Optional, List


class Vehicle(BaseModel):
    plate: str
    brand: str
    model: str
    doors: int
    vehicle_type: str
