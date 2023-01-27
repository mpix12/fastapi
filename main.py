from fastapi import FastAPI, Depends
from routers import blog_get
from routers import blog_post
from routers import user
from routers import article
from routers import product
from routers import blob_file

from db import models
from db import database
from auth import authentication
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(authentication.router)
app.include_router(blob_file.router)


@app.get('/blog')
def index(inject_dependency: dict = Depends(blog_post.required_functionality)):
    return {"message": f"Hello World, Injected dependency {inject_dependency}"}


# Files statically available:
app.mount('/media', StaticFiles(directory="media"), name='media')

models.Base.metadata.create_all(database.engine)

'''
Import: from fatsAPI import FastAPI, status, Response.

GET:
- Path parameters: passed to the path / URL. 
  Example: /blog/{id}
  validation can be added to the method. Order is important.

- Predefined values: Can be denied simply with enums.
- Query parameters: Parameters passed after the path. blog/all?page=2&page_size=10. Optional parameters can be passed.

Better documentation:
Tags: Tags are used to categories the operations, looks better in the docs sections.
Summary: -
Description: -
Response_Description: -
Add docstring to teh function.

Routers: Refactors /  components / modules.

routers: Create a directory
 blog_get: create routers - import APIRouter
 blog_post: create routers - import APIRouter
main.py: Add entries to main.py - app.include_router()

Request Body: post - BaseModel
Request Body with - Path and Query parameters:

Validators can be added.
'''

'''
Dependencies: Databases and Authentication.

SQLAlchemy: 
create_user [POST] --> userRequest [Schema] --> Database User [Model] --> db --> UserResponse. 
db Checklist:

database.py: Database definition. engine / session local / base.
models.py: Model definition. Create models / tables.
main.py: Create db. models.Base.metadata.create_all(db.engine).
schemas.py : Schema definition.
user_db.py: ORM Functionality.
user.py : API Functionality.
'''

'''
Relationship DB:
Instead of writing joins and use in the query: We can define the db relationships. 
'''