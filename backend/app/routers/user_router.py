from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, dependencies

router = APIRouter()

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
 # Check if a user with the provided phone number already exists
    existing_user = db.query(models.User).filter(models.User.phone_number == user.phone_number).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this phone number already exists."
        )

    # Create a new user instance with the provided name and phone number
    new_user = models.User(name=user.name, phone_number=user.phone_number)

    # Add the new user to the database session and commit
    db.add(new_user)
    db.commit()

    # Refresh to get the new user from the database, with the ID
    db.refresh(new_user)

    # Return the created user
    return new_user

@router.get("/users/", response_model=list[schemas.User])
def list_users(db: Session = Depends(dependencies.get_db)):
    # Retrieve and return a list of all users in the database
    users = db.query(models.User).all()
    return users