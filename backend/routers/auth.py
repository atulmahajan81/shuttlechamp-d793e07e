# routers/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.schemas import OrganizerCreate, Token, TokenRefresh
from backend.models import Organizer
from backend.auth import verify_password, get_password_hash, create_access_token, create_refresh_token
from backend.database import get_db
from backend.tasks import send_welcome_email

router = APIRouter()

@router.post("/register", response_model=dict)
async def register_user(user: OrganizerCreate, db: AsyncSession = Depends(get_db)):
    query = select(Organizer).where(Organizer.email == user.email)
    result = await db.execute(query)
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already registered.",
        )

    new_user = Organizer(
        email=user.email,
        password_hash=get_password_hash(user.password)
    )
    db.add(new_user)
    await db.commit()
    send_welcome_email.delay(user.email)
    return {"message": "User registered successfully."}