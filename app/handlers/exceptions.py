from starlette.requests import Request
from starlette.responses import JSONResponse

from app.exceptions import UnexpectedDockerError


def handle_docker_exception(_: Request, exc: UnexpectedDockerError):
    return JSONResponse(
        content={
            "detail": exc.message,
        },
        status_code=exc.status
    )
