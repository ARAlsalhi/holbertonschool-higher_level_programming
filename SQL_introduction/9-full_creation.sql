-- FULL Creation
-- I create a sconde table here 
CREATE TABLE IF NOT EXISTS second_table (
    id INT, 
    name VARCHAR(256), 
    score INT
    constraint pk_id PRiMARY KEY (id)
);

-- Add new Row 

INSERT INTO second_table 
    (id, name, score) VALUES (1, 'John', 10),
    (id, name, score) VALUES (2, 'Alex', 3),
    (id, name, score) VALUES (1, 'Bob', 14),
    (id, name, score) VALUES (1, 'George', 8);
