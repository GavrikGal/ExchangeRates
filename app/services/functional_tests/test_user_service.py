import pytest

from app.services.user_service import UserService
from app.utils.unitofwork import UnitOfWork


@pytest.mark.asyncio(scope="session")
class TestUserService:
    """ Тестирование функционала сервиса сохранения и получения пользователей """

    async def test_add_user(self, test_user_data_pydantic):
        """ Функционал сохранения пользователя """

        uow = UnitOfWork()

        user_service = UserService(uow)
        user_from_service = await user_service.add_user(test_user_data_pydantic)
        assert user_from_service.username == test_user_data_pydantic.username

