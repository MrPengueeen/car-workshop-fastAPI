from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, crud
import dependencies

router = APIRouter(
    prefix="/api/v1/users",
    tags=["users"],
)

@router.get("", response_model=list[schemas.User])
async def get_users(db: Session=Depends(dependencies.get_db)):
    return crud.get_mechanics(db=db)

@router.post("/register", response_model=schemas.User)
async def register_user(user: schemas.UserCreate, db: Session=Depends(dependencies.get_db)):
    return crud.register_user(db=db, user=user)

@router.post("/login", response_model=schemas.User)
async def login_user(user: schemas.UserLogin, db: Session=Depends(dependencies.get_db)):
    return crud.login_user(db=db, user=user)

@router.post("/login/admin", response_model=schemas.User)
async def login_admin(user: schemas.UserLogin, db: Session=Depends(dependencies.get_db)):
    return crud.login_admin(db=db, user=user)