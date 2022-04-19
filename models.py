from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Address(Base):
    """
    Create an Address model with fields
    """
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    coordinates = Column(String)
    house_no = Column(Integer)
    street = Column(String)
    city = Column(String)
    country = Column(String)
