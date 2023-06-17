import sys

sys.path.append("...")

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .auth import get_current_user

router = APIRouter(
    prefix='/api/address',
    tags=['address'],
    responses={404: {"description": "Not found"}}
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Address(BaseModel):
    address1: str
    address2: Optional[str]
    city: str
    state: str
    country: str
    postalcode: str


@router.post("")
async def create_address(address: Address, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    address_model = models.Address()
    address_model.address1 = address.address1
    address_model.address2 = address.address2
    address_model.city = address.city
    address_model.state = address.state
    address_model.country = address.country
    address_model.postalcode = address.postalcode
    db.add(address_model)
    db.flush()
    user_model = db.query(models.Users).filter(models.Users.id == user.get('id')).first()
    user_model.address_id = address_model.id
    db.add(user_model)
    db.commit()
