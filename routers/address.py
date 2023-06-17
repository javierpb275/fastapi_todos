import sys

sys.path.append("...")

from typing import Optional
from fastapi import APIRouter, Depends
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
