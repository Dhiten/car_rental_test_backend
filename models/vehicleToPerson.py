from config.database import Base
from sqlalchemy import Column, Integer,Boolean, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class VehicleToPerson(Base):
    __tablename__ = 'vehicle_person'
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    date = Column(Date, nullable=False)
    active = Column(Boolean, nullable=False)
    person = relationship("Person", back_populates="vehicules")
    vehicule = relationship("Vehicle", back_populates="people")

