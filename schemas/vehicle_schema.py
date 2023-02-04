from schemas.person import PersonSchema
from schemas.vehicle import Vehicle
from typing import Optional, List

class VehicleSchema(Vehicle):
  people: List[PersonSchema] = []