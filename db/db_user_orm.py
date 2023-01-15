from sqlalchemy.orm import Session

import Hash
from schemas import userBase
from db.models import DBUser
from Hash import bcrypt_passwd, verify
from fastapi import HTTPException, status


# Create User
def create_user(db: Session, request: userBase):
    new_user = DBUser(
        username=request.username,
        email=request.email,
        passwd=bcrypt_passwd(request.passwd)
        # passwd=request.passwd
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# Get all users
def get_all_users(db: Session):
    return db.query(DBUser).all()


# Get one user
def get_user(db: Session, id: int):
    user = db.query(DBUser).filter(DBUser.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f' user with id:{id} not found'
        )
    return user


# Get user by username
def get_user_by_username(db: Session, username: str):
    user = db.query(DBUser).filter(DBUser.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'user with username: {username} not found'
        )
    return user


# Delete a user:
def remove_user(db: Session, id: int):
    user = db.query(DBUser).filter(DBUser.id == id).first()
    db.delete(user)
    db.commit()
    return 'OK'


# Update a user:
def updated_user(db: Session, id: int, request: userBase):
    temp_dict = {
        DBUser.username: request.username,
        DBUser.email: request.email,
        DBUser.passwd: Hash.bcrypt_passwd(request.passwd)
    }
    ext_user = db.query(DBUser).filter(DBUser.id == id)
    ext_user.update(temp_dict)
    db.commit()
    return 'OK'
