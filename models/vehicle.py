from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.vehicleToPerson import VehicleToPerson


class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String)
    doors = Column(Integer)
    vehicle_type = Column(String)
    plate = Column(String)
    people = relationship("VehicleToPerson", back_populates="vehicule")