from typing import List

from fastapi import APIRouter
from fastapi import Depends
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse

from app.schemas.container import ContainerModel
from app.security.context import get_current_username
from app.utils.dependencies import DockerUtilsDependencyMarker
from app.utils.docker_utils import DockerUtils

docker_router = APIRouter(dependencies=[Depends(get_current_username)])


@docker_router.get(
    "/containers",
    summary="Get all containers",
    response_model=List[ContainerModel],
)
async def get_all_logs_from_container(
    docker_utils: DockerUtils = Depends(DockerUtilsDependencyMarker),
):
    return docker_utils.get_containers()


@docker_router.get(
    "/containers/{container_id}/logs",
    summary="Get all logs from container",
    response_class=PlainTextResponse
)
async def get_all_logs_from_container(
    container_id: str,
    docker_utils: DockerUtils = Depends(DockerUtilsDependencyMarker),
):
    return docker_utils.get_logs(container_id=container_id)


@docker_router.post(
    "/containers/{container_id}/reload",
    summary="Reload container",
    response_class=PlainTextResponse
)
async def reload_container(
    container_id: str,
    docker_utils: DockerUtils = Depends(DockerUtilsDependencyMarker),
):
    docker_utils.reload_container(container_id=container_id)
    return JSONResponse(status_code=201, content={"detail": "Task created"})
