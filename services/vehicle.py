from models.vehicle import Vehicle as VehicleModel
from schemas.vehicle import Vehicle

class VehicleService():

    
    def get(self):
        vehicles = self.query(VehicleModel).all()

        self.close()
        return vehicles

    def get_vehicle(self, id: int):
        vehicle = self.query(VehicleModel).filter(VehicleModel.id == id).first()

        self.close()
        return vehicle

    def create(self, vehicle: Vehicle):
        new_vehicle = VehicleModel(**vehicle.dict())

        self.add(new_vehicle)
        self.commit()
        self.refresh(new_vehicle)
        self.close()
        return new_vehicle

    def update(self, id: int, vehicle: Vehicle):
        vehicle_db = self.query(VehicleModel).filter(VehicleModel.id == id).first()

        vehicle_db.plate = vehicle.plate if vehicle.plate else vehicle_db.plate
        vehicle_db.brand = vehicle.brand if vehicle.brand else vehicle_db.brand
        vehicle_db.model = vehicle.model if vehicle.model else vehicle_db.model
        vehicle_db.doors = vehicle.doors if vehicle.doors else vehicle_db.doors
        vehicle_db.vehicle_type = vehicle.vehicle_type if vehicle.vehicle_type else vehicle_db.vehicle_type

        self.commit()
        self.close()
        return vehicle_db

    def delete(self, id: int):
        vehicle_db = self.query(VehicleModel).filter(VehicleModel.id == id).first()
        
        self.delete(vehicle_db)
        self.commit()
        self.close()
        return vehicle_db

