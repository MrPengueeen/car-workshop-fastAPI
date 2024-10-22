from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, crud
import dependencies

router = APIRouter(
    prefix="/api/v1/bookings",
    tags=["users"],
)


@router.get("", response_model=list[schemas.Booking])
async def get_bookings(mechanic_id: int | None = None, skip: int=0, limit: int=100, db: Session=Depends(dependencies.get_db)):
    if not mechanic_id:
        return crud.get_bookings(db=db, skip=skip, limit=limit)
    return crud.get_bookings_by_mechanic(db=db, mechanic_id=mechanic_id, skip=skip, limit=limit)

@router.post("", response_model=schemas.Booking)
async def create_booking(booking: schemas.BookingCreate, db: Session=Depends(dependencies.get_db)):
    return crud.create_booking(db=db, booking=booking)

