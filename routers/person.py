from fastapi import APIRouter
from config.database import Base, engine, Session
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.person import PersonCreate
from services.person import PersonService
from middlewares.jwt_handler import JWTHandler
from fastapi import Depends, Path, Query

person_router = APIRouter()

# CRUD person   
@person_router.post('/person', tags = ['Person'],  dependencies=[Depends(JWTHandler)])
def create_person(person: PersonCreate):
    db = Session()
    person.date_of_birth = datetime.strptime(person.date_of_birth, '%m/%d/%Y')
    new_person = PersonService.create_person(db, person)
    return JSONResponse(status_code=201, content={"message": "Person created successfully"})

@person_router.get('/person', tags = ['Person'])
def get_person():
    db = Session()
    person = PersonService.get_persons(db)
    return JSONResponse(status_code=200, content=jsonable_encoder(person))

@person_router.get('/person/{id}', tags = ['Person'])
def get_person_by_id(id: int):
    db = Session()
    person = PersonService.get_person(db, id)
    if not person:
        return JSONResponse(status_code=404, content={"message": "Person not found"})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(person))


@person_router.put('/person/{id}', tags = ['Person'], dependencies=[Depends(JWTHandler)])
def update_person(person: PersonCreate):
    db = Session()
    result= PersonService.get_person(db, id)
    if not person:
        return JSONResponse(status_code=404, content={"message": "Person not found"})
    else:
        PersonService.update_person(db, id, person)
        return JSONResponse(status_code=200, content={"message": "Person updated successfully"})

@person_router.delete('/person/{id}', tags = ['Person'], dependencies=[Depends(JWTHandler)])
def delete_person(person: PersonCreate):
    db = Session()
    result= PersonService.get_person(db, id)
    if not person:
        return JSONResponse(status_code=404, content={"message": "Person not found"})
    else:
        PersonService.delete_person(db, id)
        return JSONResponse(status_code=200, content={"message": "Person deleted successfully"})