-- script lists the number of records with the same score in the table second_table in MySQL server.
-- the records are ordered by count in decending order.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
