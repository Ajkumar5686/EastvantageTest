from typing import List, Optional

from pydantic import BaseModel


class AddressBase(BaseModel):
    """
        Added response schema for Address model
    """
    id: int
    coordinates: str
    house_no: Optional[int] = None
    street: Optional[str] = None
    city: str
    country: str

    class Config:
        orm_mode = True


class AddressCreate(BaseModel):
    """
        Added request schema for create Address
    """
    coordinates: str
    house_no: Optional[int] = None
    street: Optional[str] = None
    city: str
    country: str
