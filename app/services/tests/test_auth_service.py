import pytest
from unittest.mock import patch


from app.services.auth_service import AuthService


@pytest.mark.asyncio(scope='session')
class TestAuthService:
    """ Модульное тестирование сервиса аутентификации """

    async def test_authenticate_called_get_user_func(self, test_user_login_schema,
                                                     mock_user_service):
        """ Функция authenticate() вызывает метод get_user() сервиса пользователя """
        await AuthService.authenticate(test_user_login_schema)
        mock_user_service.get_user.assert_awaited_once()
