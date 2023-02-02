from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
app.title = "car_rental_api"
app.description = "API for car rental system"
app.version = "0.0.1"


class Vehicle(BaseModel):
    plate: str
    brand: str
    model: str
    doors: int
    vehicle_type: str

class person(BaseModel):
    id: int
    name: str
    last_name: str
    date_of_birth: str
    identification: str
    profession: str
    married: bool
    monthly_income: float
    current_vehicle: int
    history_vehicle: list



@app.get('/', tags = ['Home'])
def message():

    return {"message": "Hello World"}

# CRUD person   
@app.post('/person', tags = ['Person'])
def create_person(person: person):
    return person

@app.get('/person', tags = ['Person'])
def get_person():
    return person

@app.put('/person', tags = ['Person'])
def update_person(person: person):
    return person

@app.delete('/person', tags = ['Person'])
def delete_person(person: person):
    return person

# CRUD vehicle
@app.post('/vehicle', tags = ['Vehicle'])
def create_vehicle(vehicle: Vehicle):
    return vehicle

@app.get('/vehicle', tags = ['Vehicle'])
def get_vehicle():
    return vehicle

@app.put('/vehicle', tags = ['Vehicle'])
def update_vehicle(vehicle: Vehicle):
    return vehicle

@app.delete('/vehicle', tags = ['Vehicle'])
def delete_vehicle(vehicle: Vehicle):
    return vehicle


