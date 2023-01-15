from fastapi import APIRouter, Response, status
from typing import Optional
from enum import Enum

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.get(
        '/all',
        tags=["blog all"])
async def say_hello_all():
    return {'Message': "All ids are provided"}


@router.get(
        '/all_details',
        tags=["blog all"]
        )
def get_all_details(page=1, page_size: Optional[int] = None):
    return {"Message": f"All ids are provides on page: {page} with page_size: {page_size}"}


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    )
async def say_hello(id: int, response: Response):
    """
    **If id is greater than 5, 404 is sent, else 200**

    - param id: Mandatory
    - param response: Mandatory
    - return: 200
    """
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error": f"ID {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
    return {"message": f"Hello, {id}"}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get(
    "/type/{type}",
    summary="Retrieve all blogs",
    description="This api helps to simulates fetching all the blogs",
    response_description="All Blogs"
    )
def get_blog_type(type: BlogType):
    return {"Message": f"Blog type is {type}"}

