
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from database.connection import get_db
from models.user import User
from schemas.user_schema import (
    UserCreate,
    UserUpdate,
    UserResponse
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Create User
@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        (User.email == user.email) |
        (User.phone_no == user.phone_no)
    ).first()

    if existing_user:
        if existing_user.email == user.email:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

        if existing_user.phone_no == user.phone_no:
            raise HTTPException(
                status_code=400,
                detail="Phone number already registered"
            )

    new_user = User(
        name=user.name,
        email=user.email,
        phone_no=user.phone_no,
        password=user.password,
        salt=user.salt,
        role=user.role,
        status=user.status,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# Get All Users
@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):

    return db.query(User).all()


# Get User By ID
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# Update User

@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    # Check whether user exists
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Get only the fields provided in request
    update_data = user_data.model_dump(exclude_unset=True)

    # Check duplicate email
    if "email" in update_data:
        duplicate_email = db.query(User).filter(
            User.email == update_data["email"],
            User.id != user_id
        ).first()

        if duplicate_email:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

    # Check duplicate phone number
    if "phone_no" in update_data:
        duplicate_phone = db.query(User).filter(
            User.phone_no == update_data["phone_no"],
            User.id != user_id
        ).first()

        if duplicate_phone:
            raise HTTPException(
                status_code=400,
                detail="Phone number already registered"
            )

    # Update user fields
    for key, value in update_data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user



# Delete User
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }
