from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine
from typing import Annotated
from routers import users, bookings


models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(users.router)
app.include_router(bookings.router)

@app.get('/')
async def root():
    return {'message': 'Welcome to Ichiban Auto car workshop'}

