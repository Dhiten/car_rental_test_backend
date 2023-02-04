from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    identification = Column(String)
    profession = Column(String)
    married = Column(Boolean)
    monthly_income = Column(Float)
    current_vehicle_id = Column(Integer, ForeignKey("vehicle.id"))
    vehicules = relationship("Vehicle", secondary= "vehicle_person", back_populates="person")
