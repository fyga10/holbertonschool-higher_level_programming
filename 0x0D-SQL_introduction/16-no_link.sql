-- List all the records of the table the records has to have name.
SELECT score, name FROM second_table HAVING name IS NOT NULL ORDER BY score DESC;
