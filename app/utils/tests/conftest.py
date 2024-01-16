import pytest
from unittest.mock import patch, AsyncMock

from app.utils.unitofwork import UnitOfWork


@pytest.fixture
def uow():
    return UnitOfWork()

@pytest.fixture
def mock_session_maker():
    with patch('app.utils.unitofwork.async_session_maker') as session_maker_instance:
        session_maker_instance.return_value = AsyncMock()
        yield session_maker_instance


@pytest.fixture
def mock_user_repository():
    with patch('app.utils.unitofwork.UserRepository') as mock_user_repository:
        yield mock_user_repository
