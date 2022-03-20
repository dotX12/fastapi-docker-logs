from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    BASIC_AUTH_USERNAME: str = Field(env='BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD: str = Field(env='BASIC_AUTH_PASSWORD')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class SettingsDependencyMarker:
    pass


