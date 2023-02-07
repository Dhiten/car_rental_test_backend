from schemas.person import Person
from schemas.vehicle import Vehicle
from typing import Optional, List

class VehicleSchema(Vehicle):
  people: List[Person] = []