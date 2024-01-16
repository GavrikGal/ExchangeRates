import pytest


@pytest.mark.asyncio(scope='session')
@pytest.mark.usefixtures('mock_user_repository', 'mock_session_maker')
class TestUnitOfWork:
    """ Модульные тесты утилиты Unit of Work.
        Инициализация UoW происходит в фикстуре - объект доступен по имени uow """

    async def test_session_factory_is_available(self, uow):
        """ Фабрика сессий доступна утилите UoW """
        assert uow.session_factory is not None

    async def test_in_context_manager_session_is_available(self, uow):
        """ Утилита Uow может работать как контекстный менеджер,
            при этом инициализируется сессия """
        async with uow:
            assert uow.session is not None

    async def test_in_context_manager_user_repository_is_available(self, uow):
        """ В контекстном менеджере доступен репозиторий пользователя """
        async with uow:
            assert uow.user is not None

    async def test_exit_from_context_manager_calls_rollback(self, uow):
        """ При выходе из контекстного менеджера вызывается ролбэк сессии """
        async with uow:
            ...
        uow.session.rollback.assert_awaited_once()

    async def test_exit_from_context_manager_close_session(self, uow):
        """ При выходе из контекстного менеджера закрывается сессия """
        async with uow:
            ...
        uow.session.close.assert_awaited_once()

    async def test_in_context_manager_can_call_commit_session(self, uow):
        """ В контекстном менеджере можно вызывать коммит сессии """
        async with uow:
            await uow.commit()
        uow.session.commit.assert_awaited_once()
