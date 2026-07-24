-- List the data that not return NULL
SELECT score, name
FROM second_table
WHERE name != 'NULL'
ORDER BY score DES;
