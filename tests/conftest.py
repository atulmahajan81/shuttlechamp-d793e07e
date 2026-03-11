# pytest fixtures for FastAPI application

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from asgi_lifespan import LifespanManager
from fastapi import FastAPI

from backend.database import Base
from backend.main import app
from backend.auth import create_access_token, create_refresh_token

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(DATABASE_URL, future=True)
TestingSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

@pytest.fixture(scope="function")
async def db_session():
    async with TestingSessionLocal() as session:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        yield session
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture(scope="function")
async def async_client(db_session: AsyncSession):
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://testserver") as client:
            yield client

@pytest.fixture
def access_token():
    return create_access_token("test_user@example.com")

@pytest.fixture
def refresh_token():
    return create_refresh_token("test_user@example.com")

@pytest.fixture
def auth_headers(access_token):
    return {
        "Authorization": f"Bearer {access_token}"
    }