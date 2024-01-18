import pytest

from app.api.schemas.user import UserCreate, UserFromDB, UserLogin, UserRegistered


@pytest.fixture
def test_user_login_schema(test_user_data):
    user_login = UserLogin(username=test_user_data['username'],
                           password=test_user_data['password'])
    return user_login


@pytest.fixture
def test_user_registered_schema(test_user_data):
    user_reg = UserRegistered.model_validate(test_user_data)
    return user_reg


@pytest.fixture
def test_user_create_schema(test_user_data):
    user_create = UserCreate(username=test_user_data['username'],
                            password=test_user_data['password'])
    return user_create


@pytest.fixture
def test_user_from_db_schema(test_user_from_db_data):
    user_from_db = UserFromDB.model_validate(test_user_from_db_data)
    return user_from_db


@pytest.fixture
def test_user_from_db_data():
    user_from_db_data = {
        'username': 'test_username',
        'id': 1
    }
    return user_from_db_data


@pytest.fixture
def test_user_data():
    user_data = {
        'username': 'test_username',
        'password': 'test_password'
    }
    return user_data


@pytest.fixture
def gal_data():
    user_data = {
        'username': 'test_gal',
        'password': 'test_password'
    }
    return user_data


@pytest.fixture
def shaitan_data():
    user_data = {
        'username': 'test_shaitan',
        'password': 'test_password'
    }
    return user_data
