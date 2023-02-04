from models.vehicleToPerson import VehicleToPerson as VehiclePersonModel
from schemas.vehicleToPerson import VehiclePerson

class VehicleToPerson():

    def __self__(self, db) -> None:
        self.db = db

    def get(self):
        vehicle_persons = self.db.query(VehiclePersonModel).all()

        self.db.close()
        return vehicle_persons

    def get_People_by_vehicle(self, vehicle_id: int):
        vehicle_person = self.db.query(VehiclePersonModel).filter(VehiclePersonModel.vehicle_id == vehicle_id).first()

        self.db.close()
        return vehicle_person

    def get_vehicles_by_person(self, person_id: int):
        vehicle_person = self.db.query(VehiclePersonModel).filter(VehiclePersonModel.person_id == person_id).first()

        self.db.close()
        return vehicle_person

    def get_vehicleToPerson(self, vehicle_id: int, person_id: int):
        vehicle_person = self.db.query(VehiclePersonModel).filter(VehiclePersonModel.vehicle_id == vehicle_id, VehiclePersonModel.person_id == person_id).first()

        self.db.close()
        return vehicle_person

    def create(self, vehicle_person: VehiclePerson):
        vehicle_person = VehiclePersonModel(**vehicle_person.dict())

        self.db.add(vehicle_person)
        self.db.commit()
        self.db.close()
        return vehicle_person

    def update(self, vehicle_person: VehiclePerson):
        self.db.query(VehiclePersonModel).filter(VehiclePersonModel.vehicle_id == vehicle_person.vehicle_id, VehiclePersonModel.person_id == vehicle_person.person_id).update(vehicle_person.dict())

        self.db.commit()
        self.db.close()
        return vehicle_person

    def delete(self, vehicle_id: int, person_id: int):
        self.db.query(VehiclePersonModel).filter(VehiclePersonModel.vehicle_id == vehicle_id, VehiclePersonModel.person_id == person_id).delete()
        
        self.db.commit()
        self.db.close()
        return True