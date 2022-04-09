from datetime import datetime
from typing import Any
from typing import List

from pydantic import Field

from app.schemas.base import BaseModelORM


class ContainerState(BaseModelORM):
    Status: str
    Running: bool
    Paused: bool
    Restarting: bool
    OOMKilled: bool
    Dead: bool
    Pid: int
    ExitCode: int
    Error: str
    StartedAt: datetime
    FinishedAt: datetime


class ContainerArgs(BaseModelORM):
    Id: str
    Created: datetime
    Path: str
    Args: List[str]
    State: ContainerState
    Image: str
    ResolvConfPath: str
    HostnamePath: str
    HostsPath: str
    LogPath: str
    Name: str
    RestartCount: int
    Driver: str
    Platform: str
    HostConfig: Any
    GraphDriver: Any
    Mounts: Any
    config: Any = Field(..., alias="Config")
    NetworkSettings: Any


class ContainerModel(BaseModelORM):
    __root__: ContainerArgs
