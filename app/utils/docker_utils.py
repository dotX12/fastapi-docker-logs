from typing import List

from docker import DockerClient
from docker.models.resource import Model as DockerModel


class DockerUtils:
    def __init__(self, client: DockerClient):
        self.client = client

    def get_containers(self) -> List[DockerModel]:
        return self.client.containers.list()

    def get_logs(self, container_id: str) -> str:
        container = self.client.containers.get(container_id=container_id)
        return container.logs()

    def reload_container(self, container_id: str) -> None:
        container = self.client.containers.get(container_id=container_id)
        container.reload()
