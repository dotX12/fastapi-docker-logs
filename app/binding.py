from fastapi import APIRouter

from app.handlers.base import docker_router

own_router_v1 = APIRouter()
own_router_v1.include_router(docker_router, tags=['Docker'])
