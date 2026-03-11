# schemas.py

from pydantic import BaseModel, EmailStr, Field, UUID4, constr
from datetime import date, datetime
from typing import Optional, List


class Token(BaseModel):
    access_token: str
    refresh_token: str


class TokenRefresh(BaseModel):
    access_token: str


class OrganizerCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class OrganizerResponse(BaseModel):
    id: UUID4
    email: EmailStr

    class Config:
        orm_mode = True


class TournamentCreate(BaseModel):
    name: str
    location: str
    start_date: date
    end_date: date


class TournamentResponse(BaseModel):
    id: UUID4
    name: str
    location: str

    class Config:
        orm_mode = True


class PlayerCreate(BaseModel):
    tournament_id: UUID4
    player_name: str


class PlayerResponse(BaseMod