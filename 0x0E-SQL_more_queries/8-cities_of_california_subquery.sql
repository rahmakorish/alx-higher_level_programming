-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id
FROM state
WHERE name = California
UNION
SELECT id, name
FROM cities
WHERE cities.state_id = state.id
ORDER BY cities.id ASC;
