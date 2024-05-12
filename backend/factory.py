from fastapi import FastAPI
from apis.base import api_router

# from .routers import users, markets, items, collections
# from .internal import admin


def create_app():
    app = FastAPI()
    app.include_router(api_router)
    # app.include_router(users.router)
    # app.include_router(markets.router)
    # app.include_router(items.router)
    # app.include_router(collections.router)
    # app.include_router(
    #     admin.router,
    #     prefix="/admin",
    #     tags=["admin"]
    # )
    
    return app
    