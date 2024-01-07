from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, dependencies

router = APIRouter()

@router.post("/groups/", response_model=schemas.GroupCreate)
def create_group(group: schemas.GroupCreate, db: Session = Depends(dependencies.get_db)):
    new_group = models.Group(name=group.name)
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    return new_group

@router.get("/groups/", response_model=list[schemas.GroupCreate])
def list_groups(db: Session = Depends(dependencies.get_db)):
    groups = db.query(models.Group).all()
    return groups


@router.post("/user_groups/", response_model=schemas.UserGroupCreate)
def add_user_to_group(user_group: schemas.UserGroupCreate, db: Session = Depends(dependencies.get_db)):
    # Check if the user-group combination already exists
    existing_relation = db.query(models.UserGroup).filter(
        models.UserGroup.user_id == user_group.user_id, 
        models.UserGroup.group_id == user_group.group_id
    ).first()
    if existing_relation:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is already in the group."
        )

    # Create a new user-group relation
    new_user_group = models.UserGroup(**user_group.dict())
    db.add(new_user_group)
    db.commit()
    db.refresh(new_user_group)
    return new_user_group

@router.get("/groups/{group_id}/users", response_model=list[schemas.User])
def list_users_in_group(group_id: int, db: Session = Depends(dependencies.get_db)):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Group not found"
        )

    # Fetch users in the group
    user_groups = db.query(models.UserGroup).filter(
        models.UserGroup.group_id == group_id
    ).all()
    user_ids = [ug.user_id for ug in user_groups]
    users = db.query(models.User).filter(models.User.id.in_(user_ids)).all()
    return users