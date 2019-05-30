/* Deleted tables if they already exist */
DROP TABLE IF EXISTS Messages CASCADE;
DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS Reactions CASCADE;
DROP TABLE IF EXISTS Mentions;

/* Create the schema for our tables */
CREATE TABLE Users (id SERIAL PRIMARY KEY,
                    token TEXT,
                    name Varchar(128) DEFAULT '');
CREATE TABLE Messages (id SERIAL PRIMARY KEY,
                      user_id INT REFERENCES Users(id),
                      message TEXT, 
                      channel Varchar(128) DEFAULT 'Thank_history',
                      sent_at TIMESTAMP);
CREATE TABLE Reactions (id SERIAL PRIMARY KEY,
                        user_id INT REFERENCES Users(id),
                        message_id INT REFERENCES Messages(id),
                        reaction Varchar(128));
CREATE TABLE Mentions (message_id INT REFERENCES Messages(id),
                       user_id INT REFERENCES Users(id));