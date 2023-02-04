from routers.person import person_router
from routers.vehicle import vehicle_router
from routers.user import user_router
from routers.vehicleToPerson import vehicle_person_router as vehicleToPerson_router

def include_routes(app) -> None:
    app.include_router(person_router)
    app.include_router(vehicle_router)
    app.include_router(user_router)
    app.include_router(vehicleToPerson_router)