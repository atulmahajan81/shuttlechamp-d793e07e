# Tests for tournament endpoints

import pytest
from datetime import date


@pytest.mark.asyncio
async def test_create_tournament(async_client, auth_headers):
    """Test creating a new tournament."""
    response = await async_client.post("/api/v1/tournaments", json={
        "name": "Open Championship",
        "location": "New York",
        "start_date": str(date.today()),
        "end_date": str(date.today())
    }, headers=auth_headers)
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_list_tournaments(async_client):
    """Test listing all tournaments."""
    response = await async_client.get("/api/v1/tournaments")
    assert response.status_code == 200
    assert "tournaments" in response.json()


@pytest.mark.asyncio
async def test_get_tournament(async_client):
    """Test getting tournament details."""
    response = await async_client.get("/api/v1/tournaments/1")
    assert response.status_code == 200
    assert "name" in response.json()


@pytest.mark.asyncio
async def test_update_tournament(async_client, auth_headers):
    """Test updating tournament details."""
    response = await async_client.put("/api/v1/tournaments/1", json={
        "name": "Updated Championship",
        "location": "Los Angeles"
    }, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Championship"


@pytest.mark.asyncio
async def test_delete_tournament(async_client, auth_headers):
    """Test deleting a tournament."""
    response = await async_client.delete("/api/v1/tournaments/1", headers=auth_headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Tournament deleted successfully."}