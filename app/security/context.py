import secrets
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBasic
from fastapi.security import HTTPBasicCredentials
from starlette import status

from config import Settings
from config import SettingsDependencyMarker

security = HTTPBasic()


def get_current_username(
    credentials: HTTPBasicCredentials = Depends(security),
    settings: Settings = Depends(SettingsDependencyMarker)
):
    correct_username = secrets.compare_digest(
        credentials.username,
        settings.BASIC_AUTH_USERNAME
    )
    correct_password = secrets.compare_digest(
        credentials.password,
        settings.BASIC_AUTH_PASSWORD
    )
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
