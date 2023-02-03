from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from config.database import Base, engine, Session
from models.vehicle import Vehicle as VehicleModel
from models.person import Person as PersonModel
from models.user import User as UserModel
from datetime import datetime
from fastapi.encoders import jsonable_encoder

app = FastAPI()
app.title = "car_rental_api"
app.description = "API for car rental system"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)

class Vehicle(BaseModel):
    plate: str
    brand: str
    model: str
    doors: int
    vehicle_type: str

class PersonCreate(BaseModel):
    name: str
    last_name: str
    date_of_birth: str
    identification: str
    profession: str
    married: bool
    monthly_income: float

@app.get('/', tags = ['Home'])
def message():

    return {"message": "Hello World"}

# CRUD person   
@app.post('/person', tags = ['Person'])
def create_person(person: PersonCreate):
    db = Session()
    person.date_of_birth = datetime.strptime(person.date_of_birth, '%m/%d/%Y')
    new_person = PersonModel(**person.dict())
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    db.close()
    return JSONResponse(status_code=201, content={"message": "Person created successfully"})

@app.get('/person', tags = ['Person'])
def get_person():
    db = Session()
    person = db.query(PersonModel).all()
    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(person))

@app.get('/person/{id}', tags = ['Person'])
def get_person_by_id(id: int):
    db = Session()
    person = db.query(PersonModel).filter(PersonModel.id == id).first()
    db.close()
    if not person:
        return JSONResponse(status_code=404, content={"message": "Person not found"})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(person))


@app.put('/person/{id}', tags = ['Person'])
def update_person(person: PersonCreate):
    db = Session()
    result= db.query(PersonModel).filter(PersonModel.id == id).first()
    if not person:
        return JSONResponse(status_code=404, content={"message": "Person not found"})
    else:
        result.name = person.name if person.name else result.name
        result.last_name = person.last_name if person.last_name else result.last_name
        result.date_of_birth = person.date_of_birth if person.date_of_birth else result.date_of_birth
        result.identification = person.identification if person.identification else result.identification
        result.profession = person.profession if person.profession else result.profession
        result.married = person.married if person.married else result.married
        result.monthly_income = person.monthly_income if person.monthly_income else result.monthly_income
        db.commit()
        db.close()
        return JSONResponse(status_code=200, content={"message": "Person updated successfully"})

@app.delete('/person/{id}', tags = ['Person'])
def delete_person(person: PersonCreate):
    db = Session()
    result= db.query(PersonModel).filter(PersonModel.id == id).first()
    if not person:
        return JSONResponse(status_code=404, content={"message": "Person not found"})
    else:
        db.delete(result)
        db.commit()
        db.close()
        return JSONResponse(status_code=200, content={"message": "Person deleted successfully"})

# CRUD vehicle
@app.post('/vehicle', tags = ['Vehicle'])
def create_vehicle(vehicle: Vehicle):
    db = Session()
    new_vehicle = VehicleModel(**vehicle.dict())
    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)
    db.close()
    return JSONResponse(status_code=201, content={"message": "Vehicle created successfully"})


@app.get('/vehicle', tags = ['Vehicle'])
def get_vehicle():
    db = Session()
    vehicle = db.query(VehicleModel).all()
    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(vehicle))

@app.get('/vehicle/{id}', tags = ['Vehicle'])
def get_vehicle_by_id(id: int):
    db = Session()
    vehicle = db.query(VehicleModel).filter(VehicleModel.id == id).first()
    db.close()
    if not vehicle:
        return JSONResponse(status_code=404, content={"message": "Vehicle not found"})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(vehicle))

@app.put('/vehicle/{id}', tags = ['Vehicle'])
def update_vehicle(vehicle: Vehicle):
    db = Session()
    result= db.query(VehicleModel).filter(VehicleModel.id == id).first()
    if not vehicle:
        return JSONResponse(status_code=404, content={"message": "Vehicle not found"})
    else:
        result.plate = vehicle.plate if vehicle.plate else result.plate
        result.brand = vehicle.brand if vehicle.brand else result.brand
        result.model = vehicle.model if vehicle.model else result.model
        result.doors = vehicle.doors if vehicle.doors else result.doors
        result.vehicle_type = vehicle.vehicle_type if vehicle.vehicle_type else result.vehicle_type
        db.commit()
        db.close()
        return JSONResponse(status_code=200, content={"message": "Vehicle updated successfully"})
    

@app.delete('/vehicle/{id}', tags = ['Vehicle'])
def delete_vehicle(vehicle: Vehicle):
    db = Session()
    result= db.query(VehicleModel).filter(VehicleModel.id == id).first()
    if not vehicle:
        return JSONResponse(status_code=404, content={"message": "Vehicle not found"})
    else:
        db.delete(result)
        db.commit()
        db.close()
        return JSONResponse(status_code=200, content={"message": "Vehicle deleted successfully"})


