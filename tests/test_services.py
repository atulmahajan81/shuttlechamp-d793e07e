# Tests for service layer

import pytest
from unittest.mock import Mock
from backend.services.user_service import UserService


@pytest.mark.asyncio
async def test_user_creation_service(db_session):
    """Test user creation service logic."""
    user_service = UserService(db_session)
    user = await user_service.create_user(email="user@example.com", password="password123", role="organizer")
    assert user.id is not None
    assert user.email == "user@example.com"


@pytest.mark.asyncio
async def test_user_creation_with_existing_email(db_session):
    """Test user creation with an existing email."""
    user_service = UserService(db_session)
    await user_service.create_user(email="user@example.com", password="password123", role="organizer")
    with pytest.raises(ValueError, match="User already exists"):
        await user_service.create_user(email="user@example.com", password="password123", role="organizer")