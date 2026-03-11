# routers/matches.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.schemas import MatchResponse, MatchScoreUpdate
from backend.models import Match
from backend.database import get_db

router = APIRouter()


@router.get("/", response_model=List[MatchResponse])
async def get_matches(
    db: AsyncSession = Depends(get_db),
    tournament_id: Optional[UUID4] = None
):
    query = select(Match)
    if tournament_id:
        query = query.where(Match.tournament_id == tournament_id)
    result = await db.execute(query)
    matches = result.scalars().all()
    return matches


@router.patch("/{match_id}/score", response_model=MatchResponse)
async def update_match_score(
    match_id: UUID4,
    score_update: MatchScoreUpdate,
    db: AsyncSession = Depends(get_db)
):
    query = select(Match).where(Match.id == match_id)
    result = await db.execute(query)
    match = result.scalars().first()

    if not match:
        raise HTTPException(status_code=404, detail="Match not found")

    match.score = score_update.score
    await db.commit()
    return match