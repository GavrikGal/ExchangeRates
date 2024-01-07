import unittest

from app.api.schemas.user import UserCreate, UserFromDB
from app.services.user_service import UserService


class TestUserService(unittest.IsolatedAsyncioTestCase):
    """ Тестирование сервиса сохранения и получения пользователей """

    @unittest.skip
    async def test_add_user(self):
        """ Тестирование возможности сохранения пользователя """

        test_user_data = UserCreate(username='test_username',
                                    password='test_password')

        user_service = UserService()
        user_from_service = await user_service.add_user(test_user_data)
        self.assertEqual(
            test_user_data.username,
            user_from_service.username
        )

