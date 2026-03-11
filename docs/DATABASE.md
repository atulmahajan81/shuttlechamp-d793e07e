# Database Schema

## Schema Overview

The ShuttleChamp database uses PostgreSQL to manage relational data and Redis for caching. The main entities include Users, Tournaments, Matches, and Players.

## Entity Relationships

- **User**: Can be an Organizer, Player, or Umpire
- **Tournament**: Created by an Organizer, consists of Matches
- **Match**: Played between Players, officiated by an Umpire

## Migration Guide

1. **Make a Migration**
   ```bash
   alembic revision --autogenerate -m "Your message"
   ```

2. **Apply Migrations**
   ```bash
   alembic upgrade head
   ```

3. **Rollback Migrations**
   ```bash
   alembic downgrade -1
   ```