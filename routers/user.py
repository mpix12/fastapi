from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import db.database
from auth import oauth2
from schemas import userBase, userBaseView
from db import db_user_orm
from db import database
from typing import List

router = APIRouter(
    prefix='/user',
    tags=['user']
)


# Create
@router.post('/', response_model=userBaseView)
async def new_user(user: userBase, db: Session = Depends(database.get_db)):
    return db_user_orm.create_user(db, user)


# Read all users
@router.get('/', response_model=List[userBaseView])
def get_all_users(db: Session = Depends(database.get_db), current_user: userBase = Depends(oauth2.get_current_user)):
    return db_user_orm.get_all_users(db)


# Read one user
@router.get('/{id}', response_model=userBaseView)
def get_user(id: int, db: Session = Depends(database.get_db), current_user: userBase = Depends(oauth2.get_current_user)):
    return db_user_orm.get_user(db, id)


# Update user
@router.post('{/id}/update')
def update_user(id: int, request: userBase, db: Session = Depends(database.get_db)):
    return db_user_orm.updated_user(db, id, request)


# Delete user
@router.delete('{/id}')
async def remove_user(id: int, db: Session = Depends(db.database.get_db)):
    return db_user_orm.remove_user(db, id)

