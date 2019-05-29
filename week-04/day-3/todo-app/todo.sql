/* Delete the tables if they already exists */
DROP TABLE IF EXISTS Task;

/* Create the schema for our table */
CREATE TABLE Task(tID SERIAL PRIMARY KEY, description text);

/* Populate the table with our data */
INSERT INTO Task values('walk the dog');
INSERT INTO Task values('Buy milk');
INSERT INTO Task values('Do homework');