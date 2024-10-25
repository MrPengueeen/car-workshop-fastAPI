from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
import schemas, crud
import dependencies
import datetime
from typing import Annotated

router = APIRouter(
    prefix="/api/v1/bookings",
    tags=["users"],
)


@router.post("/mechanic", response_model=list[schemas.Booking])
async def get_bookings_by_mechanic(mechanic: schemas.User, db: Session=Depends(dependencies.get_db)):
    return crud.get_bookings_by_mechanic(db=db, mechanic_id=mechanic.id)

@router.post("/range", response_model=list[schemas.Booking])
async def get_bookings_by_date_range(start: Annotated[datetime.datetime, Body(...)], end: Annotated[datetime.datetime, Body(...)], db: Session=Depends(dependencies.get_db)):
    return crud.get_bookings_by_date_range(db=db, start=start, end=end)


@router.get("", response_model=list[schemas.Booking])
async def get_bookings(mechanic_id: int | None = None, skip: int=0, limit: int=100, db: Session=Depends(dependencies.get_db)):
    if not mechanic_id:
        return crud.get_bookings(db=db, skip=skip, limit=limit)
    return crud.get_bookings_by_mechanic(db=db, mechanic_id=mechanic_id, skip=skip, limit=limit)

@router.post("", response_model=schemas.Booking)
async def create_booking(booking: schemas.BookingCreate, db: Session=Depends(dependencies.get_db)):
    return crud.create_booking(db=db, booking=booking)

