import pytest

from app.db.models import User


@pytest.mark.asyncio(scope='session')
class TestUserRepository:
    """ Модульные тесты репозитория пользователя.
        Инициализация репозитория в фикстуре - объект доступен по имени user_repository"""

    async def test_user_model_is_available(self, user_repository):
        """ Модуль пользователя установлена в репозитории """
        assert type(user_repository.model) == type(User)

    async def test_session_is_available(self, user_repository):
        """ Сессия доступна в репозитории пользователя """
        assert user_repository.session is not None

    async def test_add_one_execute_stmt(self, user_repository, test_user_data):
        """ Функция add_one отправляет состояние в БД (в сессию) """
        await user_repository.add_one(test_user_data)
        user_repository.session.execute.assert_awaited_once()

    async def test_add_one_return_some_result(self, user_repository, test_user_data):
        """ Функция add_one отправляет состояние в БД (в сессию) """
        result = await user_repository.add_one(test_user_data)
        assert result is not None
