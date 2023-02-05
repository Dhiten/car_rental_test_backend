from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import Base, engine
from routers.router import include_routes
from middlewares import add_middlewares
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.title = "car_rental_api"
app.description = "API for car rental system"
app.version = "0.0.1"
app.add_middleware(
     CORSMiddleware,
     allow_origins=["*"],
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)

add_middlewares(app)
include_routes(app)

@app.get('/', tags = ['Home'])
def message():
     return HTMLResponse('<h1>Car_services_back API</h1>')

Base.metadata.create_all(bind=engine)


