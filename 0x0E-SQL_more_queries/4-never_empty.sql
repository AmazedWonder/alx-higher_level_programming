-- creates the table id_not_null on MySQL server
-- creates a table id_not_null,database name is passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
