from fastapi import FastAPI, APIRouter
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Union


def create_app(router: APIRouter) -> FastAPI:
    app = FastAPI(
        title="FastAPI starter kit",
        description="FastAPI starter kit that is needed for every fastapi project.",
        version="1.0.0",
        middleware=make_middleware(),
    )
    init_routers(app=app, router=router)
    return app


def init_routers(app: FastAPI, router: APIRouter, version: Union[int, str] = 1) -> None:
    if isinstance(version, str) and 'v' in version:
        version = version

    elif (isinstance(version, int) or
          (isinstance(version, str) and version.isdigit())):
        version = f'v{version}'

    app.include_router(
        router,
        prefix=f"/api/{version}",
    )


origins = [
    "*",
    "http://localhost",
    "http://localhost:8080",
]


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    ]
    return middleware
