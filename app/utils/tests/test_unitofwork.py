import pytest

from app.db.database import engine, Base
from app.utils.unitofwork import UnitOfWork
from app.api.schemas.user import UserFromDB


@pytest.fixture(scope='function', autouse=True)
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture(scope='module')
async def uow():
    return UnitOfWork()


class TestUnitOfWork:
    """ Тесты утилиты UnitOfWork """

    @pytest.mark.anyio
    async def test_session_factory_is_available(self, uow: UnitOfWork):
        """ Тест наличия фабрики сессий у UOW """
        assert uow.session_factory is not None

    @pytest.mark.anyio
    async def test_uow_can_work_as_context_manager(self, uow: UnitOfWork):
        """ С утилитой UOW можно работать как с контекстным менеджером """

        user_data = {'username': 'test_username',
                     'password': 'test_password'}

        async with uow:
            user_from_db = await uow.user.add_one(user_data)
            user_to_return = UserFromDB.model_validate(user_from_db)
            await uow.commit()
            assert user_to_return.username == user_data['username']



