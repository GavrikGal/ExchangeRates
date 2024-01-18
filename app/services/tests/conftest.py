import pytest
from unittest.mock import MagicMock, Mock, patch, AsyncMock

from app.repositories.user_repository import UserRepository
from app.utils.unitofwork import UnitOfWork


@pytest.fixture
def mock_uow(test_user_from_db_data, test_user_registered_schema):
    mock_uow = MagicMock(UnitOfWork())
    mock_user_rep = Mock(spec=UserRepository)
    mock_user_rep.add_one.return_value = test_user_from_db_data
    mock_user_rep.get_one.return_value = test_user_registered_schema
    mock_uow.user = mock_user_rep

    return mock_uow


@pytest.fixture
def mock_user_service():
    with patch('app.services.auth_service.UserService') as MockUserService:
        # as MockClass:
        # instance = MockClass.return_value
        # instance.method.return_value = 'foo'
        instance = MockUserService.return_value
        instance.get_user = AsyncMock()

        yield instance
