from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import database

from schemas import ArticleBaseView, ArticleBase
from db import db_article_orm
from auth import oauth2
from schemas import userBase


router = APIRouter(
    prefix='/article',
    tags=['article']
)


@router.post('/', response_model=ArticleBaseView)
def create_article(request: ArticleBase, db: Session = Depends(database.get_db), current_user: userBase = Depends(oauth2.get_current_user)):
    return db_article_orm.create_article(db, request)


@router.get('/{id}')  # , response_model=ArticleBaseView)
def get_article(id: int, db: Session = Depends(database.get_db), current_user: userBase = Depends(oauth2.get_current_user)):
    return {
        'data': db_article_orm.get_article(id, db),
        'current_user': current_user
    }
