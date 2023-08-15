-- Groups second_table by score and calculates count
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
