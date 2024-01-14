import pytest
import pytest_asyncio

from app.utils.unitofwork import UnitOfWork
from app.api.schemas.user import UserFromDB


@pytest_asyncio.fixture(scope="session")
async def uow():
    return UnitOfWork()


@pytest.mark.asyncio(scope="session")
@pytest.mark.usefixtures('db_init', 'db_clear')
class TestUnitOfWork:
    """ Тесты утилиты UnitOfWork """

    async def test_session_factory_is_available(self, uow: UnitOfWork):
        """ Тест наличия фабрики сессий у UOW """
        assert uow.session_factory is not None

    async def test_uow_can_work_as_context_manager(self,
                                                   uow: UnitOfWork,
                                                   test_user_data):
        """ С утилитой UOW можно работать как с контекстным менеджером """

        async with uow:
            user_from_db = await uow.user.add_one(test_user_data)
            user_to_return = UserFromDB.model_validate(user_from_db)
            await uow.commit()
            assert user_to_return.username == test_user_data['username']



