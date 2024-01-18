import pytest

from app.repositories.user_repository import UserRepository
from app.api.schemas.user import UserFromDB, UserRegistered


@pytest.mark.asyncio(scope="session")
@pytest.mark.usefixtures('db_init', 'db_clear')
class TestUserRepository:
    """ Тесты репозитория пользователей """

    async def test_session_is_available(self, db_session):
        """ Тест наличие сессии в репозитории """

        user_rep = UserRepository(db_session)

        assert user_rep.session is not None

    async def test_add_user_return_user_model_with_username(self,
                                                            db_session,
                                                            test_user_data):
        """ Тест наличия имени пользователя при добавлении пользователя """

        user_rep = UserRepository(db_session)

        user_from_db = await user_rep.add_one(test_user_data)
        user_data_from_db = UserFromDB.model_validate(user_from_db)

        await db_session.close()

        assert user_data_from_db.username == test_user_data['username']

    async def test_add_user_return_user_model_with_id(self,
                                                      db_session,
                                                      test_user_data):
        """ Тест наличия id при добавлении пользователя """

        user_rep = UserRepository(db_session)

        user_from_db = await user_rep.add_one(test_user_data)
        user_data_from_db = UserFromDB.model_validate(user_from_db)

        await db_session.close()

        assert user_data_from_db.id is not None

    async def test_get_one_return_user_model_with_username(self,
                                                           db_session,
                                                           test_user_data,
                                                           user_in_db):
        """ Тест наличия имени пользователя при получении пользователя """

        user_rep = UserRepository(db_session)

        user_from_db = await user_rep.get_one(test_user_data)
        user_registered_from_db = UserRegistered.model_validate(user_from_db)

        await db_session.close()

        assert user_registered_from_db.username == test_user_data['username']
