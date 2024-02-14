-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, state_id, name
FROM state
WHERE name = California
ORDER BY cities.id ASC;
