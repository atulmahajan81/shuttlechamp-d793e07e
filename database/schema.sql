-- Enable pgcrypto extension for UUID generation
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Table: organizers
CREATE TABLE organizers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
COMMENT ON TABLE organizers IS 'Stores organizer details';
COMMENT ON COLUMN organizers.email IS 'Unique email for each organizer';

-- Table: players
CREATE TABLE players (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    tournament_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    FOREIGN KEY (tournament_id) REFERENCES tournaments(id) ON DELETE CASCADE
);
CREATE INDEX idx_players_tournament_id ON players (tournament_id);
COMMENT ON TABLE players IS 'Stores player details';

-- Table: umpires
CREATE TABLE umpires (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_umpires_name ON umpires (name);
COMMENT ON TABLE umpires IS 'Stores umpire details';

-- Table: tournaments
CREATE TABLE tournaments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL CHECK (end_date >= start_date),
    organizer_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    FOREIGN KEY (organizer_id) REFERENCES organizers(id) ON DELETE SET NULL
);
CREATE INDEX idx_tournaments_organizer_id ON tournaments (organizer_id);
CREATE INDEX idx_tournaments_start_date ON tournaments (start_date);
COMMENT ON TABLE tournaments IS 'Stores tournament details';

-- Table: matches
CREATE TABLE matches (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tournament_id UUID NOT NULL,
    umpire_id UUID NOT NULL,
    court VARCHAR(50) NOT NULL,
    scheduled_time TIMESTAMPTZ NOT NULL,
    score VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    FOREIGN KEY (tournament_id) REFERENCES tournaments(id) ON DELETE CASCADE,
    FOREIGN KEY (umpire_id) REFERENCES umpires(id) ON DELETE SET NULL
);
CREATE INDEX idx_matches_tournament_id ON matches (tournament_id);
CREATE INDEX idx_matches_umpire_id ON matches (umpire_id);
COMMENT ON TABLE matches IS 'Stores match details';

-- Trigger function to update the updated_at column
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Triggers
CREATE TRIGGER set_timestamp BEFORE UPDATE ON organizers FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER set_timestamp BEFORE UPDATE ON players FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER set_timestamp BEFORE UPDATE ON umpires FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER set_timestamp BEFORE UPDATE ON tournaments FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER set_timestamp BEFORE UPDATE ON matches FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();