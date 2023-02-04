from pydantic import BaseModel

class VehiclePerson(BaseModel):
    vehicle_id: int
    person_id: int
    date: str
    active: bool