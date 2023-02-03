from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class VehiclePerson(Base):
    __tablename__ = 'vehicle_person'
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'), primary_key=True)

