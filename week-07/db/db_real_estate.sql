/* Deleted tables if they already exist */
DROP TABLE IF EXISTS House CASCADE;
DROP TABLE IF EXISTS Price CASCADE;
DROP TABLE IF EXISTS HouseLocation CASCADE;
DROP TABLE IF EXISTS Lister CASCADE;

/* Create the schema for tables */
CREATE TABLE House (id SERIAL PRIMARY KEY,
                    type Varchar(128),
                    bedroom_num Varchar(128),
                    bathroom_num Varchar(128),
                    car_spaces Varchar(128),
                    keywords TEXT,
                    title TEXT,
                    summary TEXT);
CREATE TABLE Price (id SERIAL PRIMARY KEY,
                    house_id INT REFERENCES House(id),
                    price FLOAT,
                    price_currency TEXT,
                    price_high FLOAT,
                    price_low FLOAT,
                    price_type Varchar(128));
CREATE TABLE HouseLocation (id SERIAL PRIMARY KEY,
                            house_id INT REFERENCES House(id),
                            latitude FLOAT,
                            longitude FLOAT,
                            location_accuracy FLOAT,
                            location TEXT,
                            country TEXT,
                            city TEXT,
                            town TEXT,
                            area TEXT,
                            street TEXT);
CREATE TABLE Lister (id SERIAL PRIMARY KEY,
                    name TEXT,
                    house_id INT REFERENCES House(id),
                    price_id INT REFERENCES Price(id),
                    list_type Varchar(128),
                    post_time INT);