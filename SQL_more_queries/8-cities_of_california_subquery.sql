-- NO join is Allow

SELECT *
FROM cities
WHERE states_id = (
    SELECT id
    FROM states 
    WHERE name = 'California'
    )
ORDER BY id ASC;
