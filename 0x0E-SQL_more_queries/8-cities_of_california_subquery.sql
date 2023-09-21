-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- lists all rows of a column in a database, database name will be passed as an argument of the mysql command
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
