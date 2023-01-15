from typing import List

from pydantic import BaseModel


# Articles inside userDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True


# Users inside the ArticleDisplay
class UserArticle(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class userBase(BaseModel):
    username: str
    email: str
    passwd: str


class userBaseView(BaseModel):
    username: str
    email: str
    items: List[Article] = []

    class Config:
        orm_mode = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class ArticleBaseView(BaseModel):
    title: str
    content: str
    published: bool
    user: UserArticle

    # database into object model
    class Config:
        orm_mode = True


