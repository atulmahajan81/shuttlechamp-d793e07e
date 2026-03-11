# Tests for user CRUD operations

import pytest


@pytest.mark.asyncio
async def test_create_user(async_client, auth_headers):
    """Test creating a new user."""
    response = await async_client.post("/api/v1/users", json={
        "email": "newuser@example.com",
        "password": "newpassword",
        "role": "organizer"
    }, headers=auth_headers)
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_get_user(async_client, auth_headers):
    """Test retrieving user details."""
    # Assuming a user already created
    response = await async_client.get("/api/v1/users/1", headers=auth_headers)
    assert response.status_code == 200
    assert "email" in response.json()


@pytest.mark.asyncio
async def test_update_user(async_client, auth_headers):
    """Test updating user details."""
    response = await async_client.put("/api/v1/users/1", json={"email": "updateduser@example.com"}, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["email"] == "updateduser@example.com"


@pytest.mark.asyncio
async def test_delete_user(async_client, auth_headers):
    """Test deleting a user."""
    response = await async_client.delete("/api/v1/users/1", headers=auth_headers)
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted successfully."}