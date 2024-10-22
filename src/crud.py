from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException
import utils
import datetime



import models, schemas

# User CRUD Operations

def register_user(db: Session, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists with the given email")
    hashed_password = utils.get_password_hash(user.password)
    db_user = models.User( email=user.email, hashed_password=hashed_password, name=user.name, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(db: Session, user: schemas.UserLogin):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="No user found with the given email")
    if not utils.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if (db_user.role != "mechanic"):
        raise HTTPException(status_code=401, detail="User is not a mechanic")
    return db_user

def login_admin(db: Session, user: schemas.UserLogin):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="No user found with the email")
    if not utils.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if (db_user.role != "admin"):
        raise HTTPException(status_code=401, detail="User does not have administrative access.")

    return db_user



# Mechanics CRUD Operations

def get_mechanics(db: Session, skip: int=0, limit: int=1000):
    return db.query(models.User).filter(models.User.role=='mechanic').offset(skip).limit(limit).all()



# Bookings CRUD Operations

def get_bookings(db: Session, skip: int=0, limit: int=1000):

    db_bookings = db.query(models.Booking).offset(skip).limit(limit).all()
    for booking in db_bookings:
        db_mechanic = db.query(models.User).filter(models.User.id==booking.mechanic_id).first()
        booking.mechanic = db_mechanic
    
    return db_bookings

def get_bookings_by_mechanic(db: Session, mechanic_id: int, skip: int=0, limit: int=1000):
    db_bookings = db.query(models.Booking).filter(models.Booking.mechanic_id==mechanic_id).offset(skip).limit(limit).all()
    for booking in db_bookings:
        db_mechanic = db.query(models.User).filter(models.User.id==booking.mechanic_id).first()
        booking.mechanic = db_mechanic
    
    return db_bookings

def create_booking(db: Session, booking: schemas.BookingCreate):
    db_booking = models.Booking(
        title=booking.title, car_make=booking.car_make, car_year=booking.car_year,
        car_model=booking.car_model, car_registration=booking.car_registration, 
        customer_email=booking.customer_email, customer_name=booking.customer_name, 
        customer_phone=booking.customer_phone, start=booking.start, end=booking.end, 
        mechanic_id=booking.mechanic_id)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    db_mechanic = db.query(models.User).filter(models.User.id == booking.mechanic_id).first()
    db_booking.mechanic = db_mechanic
    return db_booking