-- script that creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT DEFAULT 1 AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
