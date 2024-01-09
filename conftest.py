import pytest_asyncio

from app.db.database import Base, engine


@pytest_asyncio.fixture(scope="session", autouse=True)
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
