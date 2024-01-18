import pytest

from app.services.user_service import UserService
from app.utils.unitofwork import UnitOfWork


@pytest.mark.asyncio(scope="session")
@pytest.mark.usefixtures('db_init', 'db_clear')
class TestUserService:
    """ Тестирование функционала сервиса сохранения и получения пользователей """

    async def test_add_user(self, test_user_create_schema):
        """ Функционал сохранения пользователя """

        uow = UnitOfWork()

        user_service = UserService(uow)
        user_from_service = await user_service.add_user(test_user_create_schema)
        assert user_from_service.username == test_user_create_schema.username

    async def test_get_user(self, test_user_login_schema, user_in_db):
        """ Функционал получения пользователя при наличии его в БД"""

        uow = UnitOfWork()

        user_service = UserService(uow)
        user_from_service = await user_service.get_user(test_user_login_schema)
        assert user_from_service.username == test_user_login_schema.username
