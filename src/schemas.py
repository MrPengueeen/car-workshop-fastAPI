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
    