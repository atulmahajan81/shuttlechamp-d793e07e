# Tests for authentication endpoints

import pytest


@pytest.mark.asyncio
async def test_register_success(async_client):
    """Test successful user registration."""
    response = await async_client.post("/api/v1/auth/register", json={
        "email": "testuser@example.com",
        "password": "strongpassword123",
        "role": "organizer"
    })
    assert response.status_code == 201
    assert response.json() == {"message": "User registered successfully."}


@pytest.mark.asyncio
async def test_register_missing_fields(async_client):
    """Test registration with missing fields."""
    response = await async_client.post("/api/v1/auth/register", json={"email": "testuser@example.com"})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_login_success(async_client):
    """Test successful login."""
    # Register the user first
    await async_client.post("/api/v1/auth/register", json={
        "email": "testuser@example.com",
        "password": "strongpassword123",
        "role": "organizer"
    })
    response = await async_client.post("/api/v1/auth/login", json={
        "email": "testuser@example.com",
        "password": "strongpassword123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()


@pytest.mark.asyncio
async def test_login_invalid_credentials(async_client):
    """Test login with invalid credentials."""
    response = await async_client.post("/api/v1/auth/login", json={
        "email": "wronguser@example.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"


@pytest.mark.asyncio
async def test_token_refresh(async_client, refresh_token):
    """Test refreshing access token using refresh token."""
    response = await async_client.post("/api/v1/auth/refresh", json={"refresh_token": refresh_token})
    assert response.status_code == 200
    assert "access_token" in response.json()


@pytest.mark.asyncio
async def test_logout(async_client, auth_headers):
    """Test successful logout."""
    response = await async_client.post("/api/v1/auth/logout", headers=auth_headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully logged out."}