--  a script that creates a table second_table
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT INTO second_table (id, name, score)
VALUES (1, "John", 10);
INSERT INTO second_table (id, name, score)
VALUES (2, "ALEX", 3);
INSERT INTO second_table (id, name, score)
VALUES (3, "BOB", 14);
INSERT INTO second_table (id, name, score)
VALUES(4, "GEORGE", 8);
