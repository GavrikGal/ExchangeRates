import pytest
import asyncio
import pytest_asyncio

from sqlalchemy import delete
from httpx import AsyncClient

from app.db.database import Base, engine
from app.db.database import async_session_maker
from app.db.models import User

from main import app


@pytest_asyncio.fixture(scope="session")
async def client():
    async with AsyncClient(app=app, base_url='http://127.0.0.1') as client:
        yield client


@pytest_asyncio.fixture(scope="session", autouse=True)
async def db_init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest_asyncio.fixture(scope="session")
async def db_session():
    async with async_session_maker() as async_session:
        yield async_session
    # await async_session.close()


async def db_async_clear():
    stmt = delete(User)

    async with async_session_maker() as async_session:
        await async_session.execute(stmt)
        await async_session.commit()
        await async_session.close()


@pytest.fixture(scope='function', autouse=True)
def db_clear():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(db_async_clear())


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
