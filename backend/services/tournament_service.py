# services/tournament_service.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models import Tournament
from backend.cache import cache_with_redis

@cache_with_redis('tournament_by_id', 300)
async def get_tournament_by_id(tournament_id: UUID4, db: AsyncSession):
    query = select(Tournament).where(Tournament.id == tournament_id)
    result = await db.execute(query)
    return result.scalars().first()