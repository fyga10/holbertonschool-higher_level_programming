-- Create a table with id unique and default 1.
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
