from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
import models.person as Person

class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String)
    doors = Column(Integer)
    vehicle_type = Column(String)
    plate = Column(String)
    person = relationship("Person", back_populates="vehicle")

# Person.vehicle = relationship("Vehicle", order_by=Vehicle.id, back_populates="person")