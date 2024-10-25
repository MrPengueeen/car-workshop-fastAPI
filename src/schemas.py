from pydantic import BaseModel
from datetime import datetime
import schemas


# User Schemas
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    role: str
    name: str

class UserLogin(UserBase):
    password: str

class User(UserBase):
    id: int
    name: str
    role: str
    email: str

    class Config:
        orm_mode = True


# Booking Schemas

class BookingBase(BaseModel):
    title: str

class BookingCreate(BookingBase):
    car_make : str
    car_model : str
    car_year : str
    car_registration : str
    customer_name : str
    customer_email : str
    customer_phone : str
    start : datetime
    end : datetime
    mechanic_id : int

class Booking(BookingBase):
    id: int
    car_make : str
    car_model : str
    car_year : str
    car_registration : str
    customer_name : str
    customer_email : str
    customer_phone : str
    start : datetime
    end : datetime
    status: str
    mechanic : schemas.User
