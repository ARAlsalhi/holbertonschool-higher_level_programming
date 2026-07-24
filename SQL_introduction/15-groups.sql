-- Combine the row that have the same score 
--By use GROUP BY Command
SELECT score 
FROM second_table
GROUP BY score as number 
ORDER BY score DESC;
