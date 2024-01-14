import pytest

from unittest.mock import Mock
from app.services.user_service import UserService


@pytest.mark.asyncio(scope="session")
class TestUserService:
    """ Модульное тестирование сервиса пользователя """

    async def test_unit_of_work_is_available(self, test_user_data_pydantic):
        """ Тестирование установки утилиты UnitOfWork """

        uow = Mock()

        user_service = UserService(uow)
        assert user_service.uow is not None

    async def test_add_user(self, test_user_data_pydantic):

        uow = Mock()

        user_service = UserService(uow)
        assert user_service.uow is not None
