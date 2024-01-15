import pytest
from unittest.mock import MagicMock, Mock

from app.repositories.user_repository import UserRepository
from app.utils.unitofwork import UnitOfWork


@pytest.fixture
def mock_uow(test_user_from_db_data):
    mock_uow = MagicMock(UnitOfWork())
    mock_user_rep = Mock(spec=UserRepository)
    mock_user_rep.add_one.return_value = test_user_from_db_data
    mock_uow.user = mock_user_rep

    return mock_uow
