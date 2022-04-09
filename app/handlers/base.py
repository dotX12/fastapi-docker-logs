from typing import List

from fastapi import APIRouter
from fastapi import Depends
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse

from app.schemas.container import ContainerModel
from app.security.context import get_current_username
from app.utils.dependencies import AioDockerDependency
from app.utils.docker_utils import AioDockerUtils

docker_router = APIRouter(dependencies=[Depends(get_current_username)])


@docker_router.get(
    "/containers",
    summary="Get all containers",
    response_model=List[ContainerModel],
)
async def get_all_logs_from_container(
    dof: AioDockerUtils = Depends(AioDockerDependency()),
):
    return await dof.get_containers()


@docker_router.get(
    "/containers/{container}/logs",
    summary="Get all logs from container",
    response_class=PlainTextResponse
)
async def get_all_logs_from_container(
    container: str,
    docker_utils: AioDockerUtils = Depends(AioDockerDependency()),
):
    data = await docker_utils.get_logs(container_id=container)
    return "".join(data)


@docker_router.get(
    "/containers/{container}/stats",
    summary="Get all logs from container",
    response_class=JSONResponse
)
async def get_all_logs_from_container(
    container: str,
    docker_utils: AioDockerUtils = Depends(AioDockerDependency()),
):
    return await docker_utils.get_stats(container_id=container)


@docker_router.post(
    "/containers/{container_id}/reload",
    summary="Reload container",
    response_class=PlainTextResponse
)
async def reload_container(
    container_id: str,
    docker_utils: AioDockerUtils = Depends(AioDockerDependency()),
):
    await docker_utils.reload_container(container_id=container_id)
    return JSONResponse(status_code=201, content={"detail": "Task created"})
