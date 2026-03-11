# services/user_service.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models import Organizer
from backend.cache import cache_with_redis

@cache_with_redis('user_by_email', 300)
async def get_user_by_email(email: str, db: AsyncSession):
    query = select(Organizer).where(Organizer.email == email)
    result = await db.execute(query)
    return result.scalars().first()