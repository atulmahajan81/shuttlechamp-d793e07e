# Tests for SQLAlchemy models

import pytest
from sqlalchemy.exc import IntegrityError
from backend.models import Organizer, Player, Tournament, Match


@pytest.mark.asyncio
async def test_create_organizer(db_session):
    """Test creating an organizer."""
    organizer = Organizer(email="organizer@example.com", password_hash="hashed_password")
    db_session.add(organizer)
    await db_session.commit()
    assert organizer.id is not None


@pytest.mark.asyncio
async def test_create_player_without_tournament(db_session):
    """Test creating a player without a tournament."""
    player = Player(name="John Doe")
    db_session.add(player)
    with pytest.raises(IntegrityError):
        await db_session.commit()


@pytest.mark.asyncio
async def test_create_tournament_with_organizer(db_session):
    """Test creating a tournament with an organizer."""
    organizer = Organizer(email="organizer@example.com", password_hash="hashed_password")
    db_session.add(organizer)
    await db_session.commit()

    tournament = Tournament(name="Championship", location="Venue", start_date="2023-01-01", end_date="2023-01-02", organizer_id=organizer.id)
    db_session.add(tournament)
    await db_session.commit()
    assert tournament.id is not None