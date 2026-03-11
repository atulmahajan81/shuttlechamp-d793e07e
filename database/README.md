# ShuttleChamp Database

## Schema Overview

The ShuttleChamp database is designed to manage sports tournaments, including organizers, players, umpires, tournaments, and matches.

### Schema Diagram Description:

- **Organizers**: Manages the details of the tournament organizers. Each organizer can host multiple tournaments.
- **Players**: Stores player information. Players are registered for specific tournaments.
- **Umpires**: Contains umpire details, each umpire can oversee multiple matches.
- **Tournaments**: Holds information about each tournament, including location and dates. Linked to an organizer.
- **Matches**: Details of each match, including schedule, court, and score. Matches are associated with a specific tournament and umpire.

### Setup Instructions:

1. **Database Initialization**:
   - Ensure PostgreSQL is installed and running.
   - Create a database named `shuttlechamp`.
   - Run the `schema.sql` file to create the schema.

2. **Migrations**:
   - Navigate to the `database/migrations` directory.
   - Configure your `alembic.ini` with your database URL.
   - Run migrations using Alembic: `alembic upgrade head`

3. **Seed Data**:
   - To seed the database with initial data, execute `seed_data.sql` or run the `seed_data.py` script.

### Scalability and Optimization:

- **Indexes**: Composite and partial indexes are utilized to optimize queries.
- **Caching**: Redis cache is recommended for hot data with a 5-minute TTL.
- **Async Tasks**: Background jobs can be managed with Celery.

For further information, consult the schema files and Alembic migration scripts.