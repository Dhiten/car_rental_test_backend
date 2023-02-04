from fastapi import APIRouter
from config.database import Base, engine, Session
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from middlewares.jwt_handler import JWTHandler
from fastapi import Depends, Path, Query
from services.vehicleToPerson import VehicleToPerson
from schemas.vehicleToPerson import VehiclePerson

vehicle_person_router = APIRouter()

#Create relationship
@vehicle_person_router.post('/vehicle_person', tags = ['VehiclePerson'], dependencies=[Depends(JWTHandler())])
def create(vehicle_person: VehiclePerson):
    db = Session()
    result = VehicleToPerson.create(db, vehicle_person)
    return JSONResponse(status_code=201, content=jsonable_encoder(result))

#Get all the relationships
@vehicle_person_router.get('/vehicle_person', tags = ['VehiclePerson'])
def get():
    db = Session()
    result = VehicleToPerson.get(db)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#Get relationship by id
@vehicle_person_router.get('/vehicle_person/{vehicle_id}/{person_id}', tags = ['VehiclePerson'])
def get_relationship(vehicle_id: int, person_id: int):
    db = Session()
    result = VehicleToPerson.get_vehicleToPerson(db, vehicle_id, person_id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Rent not found"})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))

#Get all the cars of a person
@vehicle_person_router.get('/vehicle_person/person/{person_id}', tags = ['VehiclePerson'])
def get_relationships_person(person_id: int):
    db = Session()
    result = VehicleToPerson.get_vehicles_by_person(db, person_id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Cars not found"})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))

#Get all the persons of a car
@vehicle_person_router.get('/vehicle_person/vehicle/{vehicle_id}', tags = ['VehiclePerson'])
def get_relationships_vehicle(vehicle_id: int):
    db = Session()
    result = VehicleToPerson.get_People_by_vehicle(db, vehicle_id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Persons not found"})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))

#Update relationship
@vehicle_person_router.put('/vehicle_person/{vehicle_id}/{person_id}', tags = ['VehiclePerson'], dependencies=[Depends(JWTHandler())])
def update(vehicle_person: VehiclePerson):
    db = Session()
    result= VehicleToPerson.get_vehicleToPerson(db, vehicle_person.vehicle_id, vehicle_person.person_id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Relationship not found"})
    else:
        VehicleToPerson.update(db, vehicle_person.vehicle_id, vehicle_person.person_id, vehicle_person)
        return JSONResponse(status_code=200, content=jsonable_encoder(result))

#Delete relationship
@vehicle_person_router.delete('/vehicle_person/{vehicle_id}/{person_id}', tags = ['VehiclePerson'], dependencies=[Depends(JWTHandler())])
def delete(vehicle_id: int, person_id: int):
    db = Session()
    result= VehicleToPerson.get_vehicleToPerson(db, vehicle_id, person_id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Rent not found"})
    else:
        VehicleToPerson.delete(db, vehicle_id, person_id)
        return JSONResponse(status_code=200, content=jsonable_encoder(result))