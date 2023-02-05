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
# ,  dependencies=[Depends(JWTHandler())]
@person_router.post('/person', tags = ['Person'])
def create(person: PersonCreate):
    db = Session()
    person.date_of_birth = datetime.strptime(person.date_of_birth, '%m/%d/%Y')
    result = PersonService.create(db, person)
    return JSONResponse(status_code=201, content=jsonable_encoder(result))

@person_router.get('/person', tags = ['Person'])
def get():
    db = Session()
    result = PersonService.get(db)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@person_router.get('/person/{id}', tags = ['Person'])
def get_person(id: int):
    db = Session()
    result = PersonService.get_person(db, id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Person not found"})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


@person_router.put('/person/{id}', tags = ['Person'], dependencies=[Depends(JWTHandler())])
def update(person: PersonCreate):
    db = Session()
    result= PersonService.get_person(db, person.id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Person not found"})
    else:
        PersonService.update(db, person.id, person)
        return JSONResponse(status_code=200, content=jsonable_encoder(result))

@person_router.delete('/person/{id}', tags = ['Person'], dependencies=[Depends(JWTHandler())])
def delete(person: PersonCreate):
    db = Session()
    result= PersonService.get_person(db, person.id)
    if not person:
        return JSONResponse(status_code=404, content={"message": "Person not found"})
    else:
        PersonService.delete(db, person.id)
        return JSONResponse(status_code=200, content=jsonable_encoder(result))