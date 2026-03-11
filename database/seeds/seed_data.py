import asyncio
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from myapp.models import Organizer, Player, Umpire, Tournament, Match

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/shuttlechamp"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def seed_data():
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # Add organizers
            organizer1 = Organizer(email="admin@shuttlechamp.com", password_hash="hashed_password")
            organizer2 = Organizer(email="john.doe@gmail.com", password_hash="hashed_password")
            organizer3 = Organizer(email="jane.smith@yahoo.com", password_hash="hashed_password")
            session.add_all([organizer1, organizer2, organizer3])

            # Add tournaments
            tournament1 = Tournament(name="Spring Championship", location="New York", start_date=datetime.now().date(), end_date=(datetime.now() + timedelta(days=5)).date(), organizer_id=organizer1.id)
            tournament2 = Tournament(name="Summer Showdown", location="Los Angeles", start_date=(datetime.now() + timedelta(days=10)).date(), end_date=(datetime.now() + timedelta(days=15)).date(), organizer_id=organizer2.id)
            session.add_all([tournament1, tournament2])

            # Add players
            player1 = Player(name="Alice", tournament_id=tournament1.id)
            player2 = Player(name="Bob", tournament_id=tournament1.id)
            player3 = Player(name="Charlie", tournament_id=tournament2.id)
            session.add_all([player1, player2, player3])

            # Add umpires
            umpire1 = Umpire(name="Umpire One")
            umpire2 = Umpire(name="Umpire Two")
            session.add_all([umpire1, umpire2])

            # Add matches
            match1 = Match(tournament_id=tournament1.id, umpire_id=umpire1.id, court="Court 1", scheduled_time=datetime.now() + timedelta(hours=1))
            match2 = Match(tournament_id=tournament2.id, umpire_id=umpire2.id, court="Court 2", scheduled_time=datetime.now() + timedelta(days=11, hours=2))
            session.add_all([match1, match2])

            await session.commit()

if __name__ == '__main__':
    asyncio.run(seed_data())