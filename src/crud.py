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
