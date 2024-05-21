from apis.v1 import route_blog
from apis.v1 import route_login
from apis.v1 import route_user
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(route_user.router, prefix="/user", tags=["users"])
api_router.include_router(route_blog.router, prefix="/blog", tags=["blogs"])
api_router.include_router(route_login.router, prefix="/auth", tags=["auth"])


@api_router.get("/")
def read_root():
    return {"Hello": "World"}
