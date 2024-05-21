from apis.base import api_router
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def create_app():
    app = FastAPI()
    app.include_router(api_router)
    app.mount("/static", StaticFiles(directory="static"), name="static")

    return app
