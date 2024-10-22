from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)
    role = Column(String)
    hashed_password = Column(String)


class Booking(Base):
    __tablename__ = "Bookings"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    car_make = Column(String)
    car_model = Column(String)
    car_year = Column(String)
    car_registration = Column(String)
    customer_name = Column(String)
    customer_email = Column(String)
    customer_phone = Column(String)
    start = Column(DateTime, default=datetime.datetime.now())
    end = Column(DateTime)
    mechanic_id = Column(Integer, ForeignKey("Users.id"))
