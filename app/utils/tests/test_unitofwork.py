import pytest
import pytest_asyncio

from app.utils.unitofwork import UnitOfWork
from app.api.schemas.user import UserFromDB


@pytest_asyncio.fixture(scope="session")
async def uow():
    return UnitOfWork()


@pytest.mark.asyncio(scope="session")
class TestUnitOfWork:
    """ Тесты утилиты UnitOfWork """

    async def test_session_factory_is_available(self, uow: UnitOfWork):
        """ Тест наличия фабрики сессий у UOW """
        assert uow.session_factory is not None

    async def test_uow_can_work_as_context_manager(self, uow: UnitOfWork):
        """ С утилитой UOW можно работать как с контекстным менеджером """

        user_data = {'username': 'test_username',
                     'password': 'test_password'}

        async with uow:
            user_from_db = await uow.user.add_one(user_data)
            user_to_return = UserFromDB.model_validate(user_from_db)
            await uow.commit()
            assert user_to_return.username == user_data['username']



