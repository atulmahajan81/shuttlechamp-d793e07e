# End-to-end tests

import pytest


@pytest.mark.asyncio
async def test_full_user_flow(async_client):
    """Test complete user flow: register → login → create resource → read → update → delete."""
    # Register
    register_response = await async_client.post("/api/v1/auth/register", json={
        "email": "testuser@example.com",
        "password": "password123",
        "role": "organizer"
    })
    assert register_response.status_code == 201

    # Login
    login_response = await async_client.post("/api/v1/auth/login", json={
        "email": "testuser@example.com",
        "password": "password123"
    })
    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}

    # Create Tournament
    create_response = await async_client.post("/api/v1/tournaments", json={
        "name": "New Tournament",
        "location": "City",
        "start_date": "2023-01-01",
        "end_date": "2023-01-05"
    }, headers=headers)
    assert create_response.status_code == 201
    tournament_id = create_response.json()["id"]

    # Read Tournament
    read_response = await async_client.get(f"/api/v1/tournaments/{tournament_id}", headers=headers)
    assert read_response.status_code == 200
    assert read_response.json()["name"] == "New Tournament"

    # Update Tournament
    update_response = await async_client.put(f"/api/v1/tournaments/{tournament_id}", json={
        "name": "Updated Tournament",
        "location": "New City"
    }, headers=headers)
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Updated Tournament"

    # Delete Tournament
    delete_response = await async_client.delete(f"/api/v1/tournaments/{tournament_id}", headers=headers)
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Tournament deleted successfully."}