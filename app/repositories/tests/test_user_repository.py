import unittest

from app.repositories.user_repository import UserRepository
from app.db.database import async_session_maker


@unittest.skip
class TestUserRepository(unittest.IsolatedAsyncioTestCase):
    """ Тесты репозитория пользователей """

    async def asyncSetUp(self):
        self.session = async_session_maker()

    async def asyncTearDown(self):
        await self.session.close()

    def test_session_is_available(self):
        """ Тест наличие сессии в репозитории """

        user_rep = UserRepository(self.session)

        self.assertIsNotNone(user_rep.session)

    async def test_add_user_return_user_model_with_username_and_id(self):
        """ Тест добавления пользователя """

        user_rep = UserRepository(self.session)

        user_data = {'username': 'test_username',
                     'password': 'test_password'}
        user_data_from_db = await user_rep.add_one(user_data)

        self.assertEqual(
            user_data['username'],
            user_data_from_db.username
        )
        self.assertIsNotNone(
            user_data_from_db.id
        )
