from fastapi import Depends, APIRouter
from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db
from app.utils import hash_password

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # hash the password - user.password
    hashed_password = hash_password(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    post_query = db.query(models.Post).filter(models.User.email == new_user.email)

    if post_query.first() is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"user with email: '{user.email}' already exists")

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/{uid}', response_model=schemas.UserOut)
def get_user(uid: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == uid).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {uid} does not exist")
    return user
