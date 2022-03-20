import docker
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from app.binding import own_router_v1
from app.utils.dependencies import DockerUtilsDependencyMarker
from app.utils.docker_utils import DockerUtils
from config import SettingsDependencyMarker, Settings


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
            DockerUtilsDependencyMarker: lambda: DockerUtils(
                client=docker.from_env(),
            ),
            SettingsDependencyMarker: lambda: Settings()
        }
    )

    return application


app = get_application()
