# routers/players.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.schemas import PlayerCreate, PlayerResponse
from backend.models import Player, Tournament
from backend.database import get_db
from backend.dependencies import get_current_user

router = APIRouter()


@router.post("/", response_model=PlayerResponse)
async def register_player(
    player_data: PlayerCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    query = select(Tournament).where(Tournament.id == player_data.tournament_id)
    result = await db.execute(query)
    tournament = result.scalars().first()

    if not tournament:
        raise HTTPException(status_code=404, detail="Tournament not found")

    new_player = Player(
        name=player_data.player_name,
        tournament_id=player_data.tournament_id
    )
    db.add(new_player)
    await db.commit()
    await db.refresh(new_player)
    return new_player