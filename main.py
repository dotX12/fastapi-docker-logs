from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from app.binding import own_router_v1
from app.exceptions import UnexpectedDockerError
from app.handlers.exceptions import handle_docker_exception
from config import Settings
from config import SettingsDependencyMarker


def get_application() -> FastAPI:
    application = FastAPI(
        debug=True,
        title='Docker Utils Microservice',
        version='1.0.0',
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=['*']
    )

    application.include_router(own_router_v1)
    application.dependency_overrides.update(
        {
            SettingsDependencyMarker: lambda: Settings()
        }
    )
    application.add_exception_handler(
        UnexpectedDockerError,
        handle_docker_exception
    )
    return application


app = get_application()
