DROP TABLE IF EXISTS Model;
/* Create the shcema for table */
CREATE TABLE Model (id SERIAL PRIMARY KEY,
                    title TEXT,
                    algorithm TEXT,
                    features TEXT,
                    data_size Varchar(128),
                    clf BYTEA,
                    version Varchar(128))