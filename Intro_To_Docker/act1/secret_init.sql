-- Create the table "secrets" with a single text column
CREATE TABLE secrets (
    secret TEXT
);

-- Insert the string "cyber{postgres}" into the first entry
INSERT INTO secrets (secret) VALUES ('cyber{postgres}');

-- Insert the current version of PostgreSQL into the second entry
INSERT INTO secrets (secret)
VALUES ((SELECT version()));
