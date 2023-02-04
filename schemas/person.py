from pydantic import BaseModel



class PersonCreate(BaseModel):
    name: str
    last_name: str
    date_of_birth: str
    identification: str
    profession: str
    married: bool
    monthly_income: float