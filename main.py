from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import Base, engine
from routers.router import include_routes
from middlewares import add_middlewares


app = FastAPI()
app.title = "car_rental_api"
app.description = "API for car rental system"
app.version = "0.0.1"

add_middlewares(app)
include_routes(app)

@app.get('/', tags = ['Home'])
def message():
     return HTMLResponse('<h1>Car_services_back API</h1>')

Base.metadata.create_all(bind=engine)


