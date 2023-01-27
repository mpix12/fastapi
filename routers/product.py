import time

from fastapi import APIRouter, Response, status, Cookie, Request
from typing import Optional
import time

router = APIRouter(
    prefix='/product',
    tags=['product']
)

product_list = ['Apple', 'Banana', 'Mango']


async def time_consuming_stuff():
    time.sleep(5)
    return "ok"


@router.get('/')
async def get_products():
    await time_consuming_stuff()
    data = " ".join(product_list)
    response = Response(content=data, media_type='text/plain', status_code=status.HTTP_200_OK)
    response.set_cookie(key="c_key", value="100")
    return response


@router.get('/ck')
def get_cookies(request: Request):
    ck = request.cookies
    val = str(ck['c_key'])
    response = Response(content=val, media_type='text/plain', status_code=status.HTTP_200_OK)
    return response


