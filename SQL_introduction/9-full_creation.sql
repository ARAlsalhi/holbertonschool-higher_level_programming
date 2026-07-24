-- FULL Creation
-- I create a sconde table here 
CREATE TABLE IF NOT EXISTS second_table (
    id INT NOT NULL, 
    name VARCHAR(256) NOT NULL, 
    score INT NOT NULL,
    constraint pk_id PRiMARY KEY (id)
);

-- Add new Row 

INSERT INTO second_table (id, name, score) VALUES

    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
