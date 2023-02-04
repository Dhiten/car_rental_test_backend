from fastapi import APIRouter
from models.vehicle import Vehicle as VehicleModel
from config.database import Base, engine, Session
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.vehicle import Vehicle
from services.vehicle import VehicleService

vehicle_router = APIRouter()



# CRUD vehicle
@vehicle_router.post('/vehicle', tags = ['Vehicle'])
def create_vehicle(vehicle: Vehicle):
    db = Session()
    VehicleService.create_vehicle(db, vehicle)
    return JSONResponse(status_code=201, content={"message": "Vehicle created successfully"})


@vehicle_router.get('/vehicle', tags = ['Vehicle'])
def get_vehicle():
    db = Session()
    vehicle = VehicleService.get_vehicles(db)
    return JSONResponse(status_code=200, content=jsonable_encoder(vehicle))

@vehicle_router.get('/vehicle/{id}', tags = ['Vehicle'])
def get_vehicle_by_id(id: int):
    db = Session()
    vehicle = VehicleService.get_vehicle(db, id)
    if not vehicle:
        return JSONResponse(status_code=404, content={"message": "Vehicle not found"})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(vehicle))

@vehicle_router.put('/vehicle/{id}', tags = ['Vehicle'])
def update_vehicle(vehicle: Vehicle):
    db = Session()
    result= VehicleService.get_vehicle(db, id)
    if not vehicle:
        return JSONResponse(status_code=404, content={"message": "Vehicle not found"})
    else:
        VehicleService.update_vehicle(db, id, vehicle)
        return JSONResponse(status_code=200, content={"message": "Vehicle updated successfully"})
    

@vehicle_router.delete('/vehicle/{id}', tags = ['Vehicle'])
def delete_vehicle(vehicle: Vehicle):
    db = Session()
    result= VehicleService.get_vehicle(db, id)
    if not vehicle:
        return JSONResponse(status_code=404, content={"message": "Vehicle not found"})
    else:
        VehicleService.delete_vehicle(db, id)
        return JSONResponse(status_code=200, content={"message": "Vehicle deleted successfully"})

