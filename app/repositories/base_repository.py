from abc import ABC, abstractmethod

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    """ Абстрактный репозиторий """

    @abstractmethod
    async def add_one(self, data: dict) -> dict:
        ...


class BaseRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def get_one(self, data: dict):
        query = select(self.model).where(self.model.username == data['username'])
        res = await self.session.execute(query)
        return res.scalar_one()
