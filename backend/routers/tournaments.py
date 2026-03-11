# routers/tournaments.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.schemas import TournamentCreate, TournamentResponse
from backend.models import Tournament
from backend.database import get_db
from backend.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=TournamentResponse)
async def create_tournament(
    tournament: TournamentCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_tournament = Tournament(
        name=tournament.name,
        location=tournament.location,
        start_date=tournament.start_date,
        end_date=tournament.end_date,
        organizer_id=current_user.id
    )
    db.add(new_tournament)
    await db.commit()
    await db.refresh(new_tournament)
    return new_tournament

@router.get("/", response_model=List[TournamentResponse])
async def get_tournaments(
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None
):
    query = select(Tournament).offset(skip).limit(limit)

    if search:
        query = query.where(Tournament.name.ilike(f'%{search}%'))
    result = await db.execute(query)
    tournaments = result.scalars().all()
    return tournaments