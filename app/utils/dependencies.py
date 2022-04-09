from app.utils.context import aiodocker_context
from app.utils.docker_utils import AioDockerUtils


class DockerUtilsDependencyMarker:
    pass


class AioDockerDependency:
    async def __call__(self):
        async with aiodocker_context() as _docker:
            yield AioDockerUtils(_docker)
