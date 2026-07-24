-- Combine the row that have the same score 
-- By use GROUP BY Command
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score 
ORDER BY number DESC;
