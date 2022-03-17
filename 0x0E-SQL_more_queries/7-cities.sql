CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create a database and a table.
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
       id INT UNIQUE NOT NULL AUTO_INCREMENT,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id),
       CONSTRAINT cities_ibfk_1 FOREIGN KEY (state_id)
       REFERENCES states(id)
);
