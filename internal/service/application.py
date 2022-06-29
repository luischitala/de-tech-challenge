import uuid

from internal.dto.application import BaseApplication
from internal.entity.application import Application
from package.sqlalchemy.repository import Inject, Repository


class ApplicationService(object):

    def __init__(
        self, repository: Repository[Application] = Inject(Application),
    ) -> None:
        self.repository = repository

    async def create(self, dto: BaseApplication) -> Application:
        application = self.repository.create(**dto.dict())
        return await self.repository.save(application)

    async def find_one_or_fail(self, application_id: uuid.UUID) -> Application:
        return await self.repository.find_one_or_fail(id=application_id)

    async def delete(self, application_id: uuid.UUID) -> None:
        application = await self.find_one_or_fail(application_id)
        await self.repository.delete(application)