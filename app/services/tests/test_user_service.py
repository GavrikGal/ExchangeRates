import pytest

from app.services.user_service import UserService


@pytest.mark.asyncio(scope="session")
class TestUserService:
    """ Модульное тестирование сервиса пользователя """

    async def test_unit_of_work_is_available(self, test_user_create_schema, mock_uow):
        """ Тестирование установки утилиты UnitOfWork """

        user_service = UserService(mock_uow)
        assert user_service.uow is not None

    async def test_add_user_called_add_one_rep_func(self, test_user_create_schema,
                                                    mock_uow):
        """ Функция add_user() вызывает функцию add_one() репозитория пользователя """

        user_service = UserService(mock_uow)
        await user_service.add_user(test_user_create_schema)

        user_service.uow.user.add_one.assert_awaited_once()

    async def test_add_user_called_commit_uow_func(self, test_user_create_schema,
                                                   mock_uow):
        """ Функция add_user() вызывает функцию commit() утилиты UOF """

        user_service = UserService(mock_uow)
        await user_service.add_user(test_user_create_schema)
        user_service.uow.commit.assert_awaited_once()

    async def test_add_user_returned_user_from_db_schema(self, test_user_create_schema,
                                                         mock_uow,
                                                         test_user_from_db_schema):
        """ Функция add_user() возвращает валидного пользователя """

        user_service = UserService(mock_uow)
        user_from_db = await user_service.add_user(test_user_create_schema)

        assert user_from_db == test_user_from_db_schema
