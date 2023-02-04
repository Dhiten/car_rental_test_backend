from fastapi import APIRouter
from config.database import Base, engine, Session
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.vehicle_schema import VehicleSchema as Vehicle
from services.vehicle import VehicleService
from middlewares.jwt_handler import JWTHandler
from fastapi import Depends, Path, Query

vehicle_router = APIRouter()



# CRUD vehicle
@vehicle_router.post('/vehicle', tags = ['Vehicle'], dependencies=[Depends(JWTHandler())])
def create(vehicle: Vehicle):
    db = Session()
    result=VehicleService.create(db, vehicle)
    return JSONResponse(status_code=201, content=jsonable_encoder(result))


@vehicle_router.get('/vehicles', tags = ['Vehicle'])
def get():
    db = Session()
    result = VehicleService.get(db)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@vehicle_router.get('/vehicle/{id}', tags = ['Vehicle'])
def get_vehicle(id: int):
    db = Session()
    result = VehicleService.get_vehicle(db, id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Vehicle not found"})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))

@vehicle_router.put('/vehicle/{id}', tags = ['Vehicle'], dependencies=[Depends(JWTHandler())])
def update(vehicle: Vehicle):
    db = Session()
    result= VehicleService.get_vehicle(db, vehicle.id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Vehicle not found"})
    else:
        VehicleService.update(db, vehicle.id, vehicle)
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    

@vehicle_router.delete('/vehicle/{id}', tags = ['Vehicle'], dependencies=[Depends(JWTHandler())])
def delete(vehicle: Vehicle):
    db = Session()
    result= VehicleService.get_vehicle(db, vehicle.id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Vehicle not found"})
    else:
        VehicleService.delete(db, id)
        return JSONResponse(status_code=200, content=jsonable_encoder(result))

