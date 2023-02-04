from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import Base, engine
from routers.person import person_router
from routers.vehicle import vehicle_router
from routers.user import user_router
from routers.vehicle_person import vehicle_person_router
from middlewares.error_handler import ErrorHandler

app = FastAPI()
app.title = "car_rental_api"
app.description = "API for car rental system"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

app.include_router(person_router)
app.include_router(vehicle_router)
app.include_router(user_router)
app.include_router(vehicle_person_router)

@app.get('/', tags = ['Home'])
def message():
     return HTMLResponse('<h1>Car_services_back API</h1>')

Base.metadata.create_all(bind=engine)


