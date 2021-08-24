from fastapi import FastAPI
from src.Controller import LoginController

from src.Container import Container

routes = [LoginController]

def create_app() -> FastAPI:
    container = Container()
    container.wire(modules=routes)

    app = FastAPI()
    app.container = container

    for route in routes: app.include_router(route.router)

    return app

app = create_app()