# Tests for pagination and filtering

import pytest


@pytest.mark.asyncio
async def test_list_tournaments_pagination(async_client):
    """Test pagination on list tournaments endpoint."""
    # Populate with dummy data
    for i in range(15):
        await async_client.post("/api/v1/tournaments", json={
            "name": f"Tournament {i}",
            "location": "City",
            "start_date": "2023-01-01",
            "end_date": "2023-01-05"
        })

    response = await async_client.get("/api/v1/tournaments?page=1&limit=10")
    assert response.status_code == 200
    assert len(response.json()["tournaments"]) == 10

    response = await async_client.get("/api/v1/tournaments?page=2&limit=10")
    assert response.status_code == 200
    assert len(response.json()["tournaments"]) == 5


@pytest.mark.asyncio
async def test_list_tournaments_search_filter(async_client):
    """Test search filter on list tournaments endpoint."""
    # Assuming tournaments are already created
    response = await async_client.get("/api/v1/tournaments?search=Championship")
    assert response.status_code == 200
    assert "Championship" in response.json()["tournaments"][0]["name"]