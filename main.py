from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import crud, models, schemas
from database import engine, get_db


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/address/", response_model=List[schemas.AddressBase], tags=['Get Address'])
def read_address(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get List of Address stored in the database
    """
    address = crud.AddressRepo.get_address(db, skip=skip, limit=limit)
    return address


@app.post("/address/", response_model=schemas.AddressBase, tags=['Create Address'])
def create_address(
    request: schemas.AddressCreate, db: Session = Depends(get_db)
):
    """
    Create an Address and store in the database
    """
    return crud.AddressRepo.create_address(db=db, request=request)


@app.put("/address/{address_id}", response_model=schemas.AddressBase, tags=['Update Address'])
async def update_address(
    address_id: int, request: schemas.AddressCreate, db: Session = Depends(get_db)
):
    """
    Update an Address stored in the database
    """
    db_item = crud.AddressRepo.fetch_by_id(db, address_id)
    if db_item:
        update_item_encoded = jsonable_encoder(request)
        db_item.coordinates = update_item_encoded['coordinates']
        db_item.house_no = update_item_encoded['house_no']
        db_item.street = update_item_encoded['street']
        db_item.city = update_item_encoded['city']
        db_item.country = update_item_encoded['country']
        return await crud.AddressRepo.update(db=db, item_data=db_item)
    else:
        raise HTTPException(status_code=400, detail="Address not found with the given ID")


@app.delete('/address/{address_id}', tags=['Delete Address'])
async def delete_address(address_id: int, db: Session = Depends(get_db)):
    """
    Delete the address with the given ID
    """
    db_item = crud.AddressRepo.fetch_by_id(db, address_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Address not found with the given ID")
    await crud.AddressRepo.delete(db, address_id)
    return "Address deleted successfully!"
