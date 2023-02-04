from fastapi import FastAPI
from config.database import Base, engine
from routers.person import person_router
from routers.vehicle import vehicle_router
from routers.user import user_router

app = FastAPI()
app.title = "car_rental_api"
app.description = "API for car rental system"
app.version = "0.0.1"

app.include_router(person_router)
app.include_router(vehicle_router)
app.include_router(user_router)

@app.get('/', tags = ['Home'])
def message():

    return {"message": "Hello World"}

Base.metadata.create_all(bind=engine)


