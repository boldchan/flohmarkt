from fastapi import APIRouter

from apis.v1 import route_user
from apis.v1 import route_blog

api_router = APIRouter()
api_router.include_router(route_user.router, prefix="/user", tags=["users"])
api_router.include_router(route_blog.router, prefix="/blog", tags=["blogs"])

@api_router.get("/")
def read_root():
    return {"Hello": "World"}