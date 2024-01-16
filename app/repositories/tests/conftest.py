import pytest
from unittest.mock import AsyncMock, Mock
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_repository import UserRepository


@pytest.fixture
def user_repository():
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session.execute.return_value = Mock()
    return UserRepository(mock_session)
