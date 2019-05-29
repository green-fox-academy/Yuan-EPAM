/* Delete the table if it already exists */
DROP TABLE IF EXISTS Car;

/* Create the schema for our table */
CREATE TABLE Car(id SERIAL PRIMARY KEY, 
                 brand TEXT,
                 model TEXT,
                 year INT,
                 condition TEXT,
                 price DECIMAL(10,2),
                 COUNT INT)

