from contextlib import asynccontextmanager
from aiodocker import Docker, DockerError

from app.exceptions import UnexpectedDockerError


@asynccontextmanager
async def aiodocker_context():
    docker = Docker()
    try:
        yield docker
    except DockerError as error:
        raise UnexpectedDockerError(
            message=error.message, status=error.status
        ) from error
    finally:
        await docker.close()
