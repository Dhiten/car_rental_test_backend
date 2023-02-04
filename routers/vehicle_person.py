from fastapi import APIRouter
from config.database import Base, engine, Session
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from middlewares.jwt_handler import JWTHandler
from fastapi import Depends, Path, Query
from services.vehicle_person import VehiclePersonService
from schemas.vehicle_person import VehiclePerson

vehicle_person_router = APIRouter()

#Create relationship
@vehicle_person_router.post('/vehicle_person', tags = ['VehiclePerson'], dependencies=[Depends(JWTHandler())])
def create_relationship(vehicle_person: VehiclePerson):
    db = Session()
    vehicle_person = VehiclePersonService.create_vehicle_person(db, vehicle_person)
    return JSONResponse(status_code=201, content=jsonable_encoder(vehicle_person))

#Get all the relationships
@vehicle_person_router.get('/vehicle_person', tags = ['VehiclePerson'])
def get_relationship():
    db = Session()
    vehicle_person = VehiclePersonService.get_vehicle_persons(db)
    return JSONResponse(status_code=200, content=jsonable_encoder(vehicle_person))

#Get relationship by id
@vehicle_person_router.get('/vehicle_person/{vehicle_id}/{person_id}', tags = ['VehiclePerson'])
def get_relationship_by_id(vehicle_id: int, person_id: int):
    db = Session()
    vehicle_person = VehiclePersonService.get_vehicle_person(db, vehicle_id, person_id)
    if not vehicle_person:
        return JSONResponse(status_code=404, content={"message": "Rent not found"})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(vehicle_person))

#Get all the cars of a person
@vehicle_person_router.get('/vehicle_person/person/{person_id}', tags = ['VehiclePerson'])
def get_relationship_by_person_id(person_id: int):
    db = Session()
    vehicle_person = VehiclePersonService.get_vehicle_person_listVehicles(db, person_id)
    if not vehicle_person:
        return JSONResponse(status_code=404, content={"message": "Cars not found"})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(vehicle_person))

#Get all the persons of a car
@vehicle_person_router.get('/vehicle_person/vehicle/{vehicle_id}', tags = ['VehiclePerson'])
def get_relationship_by_vehicle_id(vehicle_id: int):
    db = Session()
    vehicle_person = VehiclePersonService.get_vehicle_person_listPersons(db, vehicle_id)
    if not vehicle_person:
        return JSONResponse(status_code=404, content={"message": "Persons not found"})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(vehicle_person))

#Update relationship
@vehicle_person_router.put('/vehicle_person/{vehicle_id}/{person_id}', tags = ['VehiclePerson'], dependencies=[Depends(JWTHandler())])
def update_relationship(vehicle_person: VehiclePerson):
    db = Session()
    result= VehiclePersonService.get_vehicle_person(db, vehicle_person.vehicle_id, vehicle_person.person_id)
    if not vehicle_person:
        return JSONResponse(status_code=404, content={"message": "Relationship not found"})
    else:
        VehiclePersonService.update_vehicle_person(db, vehicle_person.vehicle_id, vehicle_person.person_id, vehicle_person)
        return JSONResponse(status_code=200, content={"message": "Relationship updated successfully"})

#Delete relationship
@vehicle_person_router.delete('/vehicle_person/{vehicle_id}/{person_id}', tags = ['VehiclePerson'], dependencies=[Depends(JWTHandler())])
def delete_relationship(vehicle_id: int, person_id: int):
    db = Session()
    result= VehiclePersonService.get_vehicle_person(db, vehicle_id, person_id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Rent not found"})
    else:
        VehiclePersonService.delete_vehicle_person(db, vehicle_id, person_id)
        return JSONResponse(status_code=200, content={"message": "Rent deleted successfully"})