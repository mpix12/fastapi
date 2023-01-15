from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from schemas import ArticleBase
from db.models import DBArticle


# Create Article:
def create_article(db: Session, request: ArticleBase):
    new_article = DBArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


# Get Article:
def get_article(id: int, db: Session):
    article = db.query(DBArticle).filter(DBArticle.id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with id {id} not found')
    return article
