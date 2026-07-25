-- 
SELECT 
    TS.title, 
    TSG.genre_id
FROM tv_shows AS TS 
INNER JOIN tv_show_genres AS TSG 
ON TS.title = TSG.genre_id 
ORDER BY TS.title ASC, TSG.genre_id ASC;
