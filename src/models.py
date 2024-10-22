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