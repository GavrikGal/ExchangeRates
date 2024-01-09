import pytest
import pytest_asyncio

from app.repositories.user_repository import UserRepository
from app.db.database import async_session_maker
from app.api.schemas.user import UserFromDB


@pytest_asyncio.fixture(scope="session")
async def session():
    async with async_session_maker() as async_session:
        yield async_session
    await async_session.close()


@pytest.mark.asyncio(scope="session")
class TestUserRepository:
    """ Тесты репозитория пользователей """

    async def test_session_is_available(self, session):
        """ Тест наличие сессии в репозитории """

        user_rep = UserRepository(session)

        assert user_rep.session is not None

    async def test_add_user_return_user_model_with_username(self, session):
        """ Тест наличия имени пользователя при добавлении пользователя """

        user_rep = UserRepository(session)

        user_data = {'username': 'test_username',
                     'password': 'test_password'}
        user_from_db = await user_rep.add_one(user_data)
        user_data_from_db = UserFromDB.model_validate(user_from_db)

        await session.close()

        assert user_data_from_db.username == user_data['username']

    async def test_add_user_return_user_model_with_id(self, session):
        """ Тест наличия id при добавлении пользователя """

        user_rep = UserRepository(session)

        user_data = {'username': 'test_username',
                     'password': 'test_password'}
        user_from_db = await user_rep.add_one(user_data)
        user_data_from_db = UserFromDB.model_validate(user_from_db)

        await session.close()

        assert user_data_from_db.id is not None
