import pytest

from app.services.auth_service import AuthService


@pytest.mark.asyncio(scope='session')
@pytest.mark.usefixtures('db_init', 'db_clear')
class TestAuthService:
    """ Тестирование функционала сервиса аутентификации пользователя """

    async def test_authenticate(self, test_user_login_schema):
        """ Функционал аутентификации """
        auth_user = await AuthService.authenticate(test_user_login_schema)
        assert auth_user is not None
