from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]


router = APIRouter(
    prefix='/blog',
    tags=['blog']
    )


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: Optional[int] = 1):
    '''
    BlogModel: RequestBody
    id: path parameter (Being defined in path / URL). /blog/{id}
    version: Query parameter. blog/new/10?version=10
    '''
    return {'Message': 'Post Message'}


def required_functionality():
    return {'Message': 'Dependency injection - Hello World'}

