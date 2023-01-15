from fastapi.param_functions import Depends
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
import jwt
from sqlalchemy.orm import Session
from db import database
from db import db_user_orm


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# (venv) mandarpande@Mandars-MacBook-Air fastApiProject % openssl rand -hex 32
SECRET_KEY = 'fc419dd75ec42a810926d904c3cb194fae1335158173ef40b7a39559d0f10d5e'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exeption = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Unauthorized access',
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exeption
    except jwt.PyJWTError:
        raise credentials_exeption

    username = db_user_orm.get_user_by_username(db, username)

    if username is None:
        raise credentials_exeption

    return username

