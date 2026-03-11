# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from backend.routers import auth, users, tournaments, players, matches
from backend.dependencies import lifespan
from backend.exceptions import setup_exception_handlers

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost",
    "http://localhost:8000",
    # Add your production origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware)

setup_exception_handlers(app)

app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(users.router, prefix="/api/v1/users")
app.include_router(tournaments.router, prefix="/api/v1/tournaments")
app.include_router(players.router, prefix="/api/v1/players")
app.include_router(matches.router, prefix="/api/v1/matches")