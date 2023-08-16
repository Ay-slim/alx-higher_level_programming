-- Create the cities DB table in the DB hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INTEGER PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL,
	state_id INTEGER NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id)
);
