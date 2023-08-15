-- Lists all second_table records with name values
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
