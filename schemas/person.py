from pydantic import BaseModel
from typing import Optional, List



class PersonCreate(BaseModel):
    name: str
    last_name: str
    date_of_birth: str
    identification: str
    profession: str
    married: bool
    monthly_income: float
    current_vehicle_id: Optional[int] = None