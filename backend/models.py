# models.py

from sqlalchemy import Column, String, DateTime, ForeignKey, UUID
from sqlalchemy.dialects.postgresql import UUID as P_UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base

import uuid


class Organizer(Base):
    __tablename__ = 'organizers'

    id = Column(P_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    tournaments = relationship('Tournament', back_populates='organizer')


class Player(Base):
    __tablename__ = 'players'

    id = Column(P_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    tournament_id = Column(P_UUID(as_uuid=True), ForeignKey('tournaments.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    tournament = relationship('Tournament', back_populates='players')


class Umpire(Base):
    __tablename__ = 'umpires'

    id = Column(P_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    matches = relationship('Match', back_populates='umpire')


class Tournament(Base):
    __tablename__ = 'tournaments'

    id = Column(P_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    organizer_id = Column(P_UUID(as_uuid=True), ForeignKey('organizers.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    organizer = relationship('Organizer', back_populates='tournaments')
    players = relationship('Player', back_populates='tournament')
    matches = relationship('Match', back_populates='tournament')


class Match(Base):
    __tablename__ = 'matches'

    id = Column(P_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tournament_id = Column(P_UUID(as_uuid=True), ForeignKey('tournaments.id'), nullable=False)
    umpire_id = Column(P_UUID(as_uuid=True), ForeignKey('umpires.id'), nullable=False)
    court = Column(String, nullable=False)
    scheduled_time = Column(DateTime, nullable=False)
    score = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    tournament = relationship('Tournament', back_populates='matches')
    umpire = relationship('Umpire', back_populates='matches')