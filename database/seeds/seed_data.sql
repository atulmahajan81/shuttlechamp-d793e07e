-- Insert Organizers
INSERT INTO organizers (id, email, password_hash) VALUES
  (gen_random_uuid(), 'admin@shuttlechamp.com', 'hashed_password'),
  (gen_random_uuid(), 'john.doe@gmail.com', 'hashed_password'),
  (gen_random_uuid(), 'jane.smith@yahoo.com', 'hashed_password');

-- Insert Tournaments
INSERT INTO tournaments (id, name, location, start_date, end_date, organizer_id) VALUES
  (gen_random_uuid(), 'Spring Championship', 'New York', CURRENT_DATE, CURRENT_DATE + INTERVAL '5 days', (SELECT id FROM organizers WHERE email = 'admin@shuttlechamp.com')),
  (gen_random_uuid(), 'Summer Showdown', 'Los Angeles', CURRENT_DATE + INTERVAL '10 days', CURRENT_DATE + INTERVAL '15 days', (SELECT id FROM organizers WHERE email = 'john.doe@gmail.com'));

-- Insert Players
INSERT INTO players (id, name, tournament_id) VALUES
  (gen_random_uuid(), 'Alice', (SELECT id FROM tournaments WHERE name = 'Spring Championship')),
  (gen_random_uuid(), 'Bob', (SELECT id FROM tournaments WHERE name = 'Spring Championship')),
  (gen_random_uuid(), 'Charlie', (SELECT id FROM tournaments WHERE name = 'Summer Showdown'));

-- Insert Umpires
INSERT INTO umpires (id, name) VALUES
  (gen_random_uuid(), 'Umpire One'),
  (gen_random_uuid(), 'Umpire Two');

-- Insert Matches
INSERT INTO matches (id, tournament_id, umpire_id, court, scheduled_time) VALUES
  (gen_random_uuid(), (SELECT id FROM tournaments WHERE name = 'Spring Championship'), (SELECT id FROM umpires WHERE name = 'Umpire One'), 'Court 1', CURRENT_TIMESTAMP + INTERVAL '1 hour'),
  (gen_random_uuid(), (SELECT id FROM tournaments WHERE name = 'Summer Showdown'), (SELECT id FROM umpires WHERE name = 'Umpire Two'), 'Court 2', CURRENT_TIMESTAMP + INTERVAL '11 days' + INTERVAL '2 hours');