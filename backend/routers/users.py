# routers/users.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.schemas import OrganizerResponse
from backend.models import Organizer
from backend.database import get_db
from backend.dependencies import get_current_user

router = APIRouter()

@router.get("/", response_model=List[OrganizerResponse])
async def get_users(
    db: AsyncSession = Depends(get_db),
    current_user: Organizer = Depends(get_current_user),
    skip: int = 0,
    limit: int = 10
):
    query = select(Organizer).offset(skip).limit(limit)
    result = await db.execute(query)
    users = result.scalars().all()
    return users

@router.get("/{user_id}", response_model=OrganizerResponse)
async def get_user(user_id: UUID4, db: AsyncSession = Depends(get_db)):
    query = select(Organizer).where(Organizer.id == user_id)
    result = await db.execute(query)
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user