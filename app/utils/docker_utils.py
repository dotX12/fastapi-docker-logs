from typing import List
from aiodocker.containers import DockerContainer
from aiodocker import Docker


class AioDockerUtils:
    def __init__(self, client: Docker):
        self.client = client

    async def get_containers(self) -> List[DockerContainer]:
        containers = await self.client.containers.list()
        return [await container.show() for container in containers]

    async def get_logs(self, container_id: str) -> List[str]:
        container = await self.client.containers.get(container=container_id)
        return await container.log(stdout=True, stderr=True)

    async def get_stats(self, container_id: str) -> List[str]:
        container = await self.client.containers.get(container=container_id)
        return await container.stats(stream=False)

    async def reload_container(self, container_id: str) -> None:
        container = await self.client.containers.get(container=container_id)
        await container.restart()
