from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    full_name = Column(String)
    is_active = Column(String)
    is_superuser = Column(String)
    person = Column(Integer, ForeignKey("person.id"))