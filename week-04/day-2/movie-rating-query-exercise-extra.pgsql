
/*
Movie ( mID, title, year, director ) 
English: There is a movie with ID number mID, a title, a release year, and a director. 

Reviewer ( rID, name ) 
English: The reviewer with ID number rID has a certain name. 

Rating ( rID, mID, stars, ratingDate ) 
English: The reviewer rID gave the movie mID a number of stars rating (1-5) on a certain ratingDate. 
*/

/* 1. Find the names of all reviewers who rated Gone with the Wind. */
SELECT DISTINCT rv.name
FROM (SELECT r.rID, m.title
      FROM Movie m INNER JOIN Rating r
          ON m.mID=r.mID) AS movie_rating INNER JOIN Reviewer rv
                                         ON movie_rating.rID=rv.rID
WHERE movie_rating.title="Gone with the Wind";

/* 2. For any rating where the reviewer is the same as the director of the movie, return the reviewer name, movie title, and number of stars. */
SELECT rv.name, movie_rating.title, movie_rating.stars
FROM (SELECT m.title, m.director, r.stars, r.rID
      FROM Rating r INNER JOIN Movie m
          ON r.mID=m.mID) AS movie_rating INNER JOIN Reviewer rv
              ON movie_rating.rID=rv.rID
WHERE movie_rating.director=rv.name;


/* 3. Return all reviewer names and movie names together in a single list, alphabetized */
SELECT rv.name
FROM reviewer rv
UNION
SELECT m.title
FROM movie m
ORDER BY name ASC;


/* 4. Find the titles of all movies not reviewed by Chiris Jackson. */
SELECT m.mID, m.title
FROM movie m
WHERE m.mid not in (SELECT DISTINCT r.mid
                   FROM reviewer rv INNER JOIN rating r
                        ON rv.rID = r.rID
                   WHERE rv.name = 'Chris Jackson'
                   ORDER BY r.mid);


/* 5. For all paris of reviewers such that both reviewers gave a 
rating to the same movie, return the names of both reviewers. Eliminate duplicates, 
don't pair reviewers with themselves, and include each pair only once. 
For each pair, return the names in the pair in alphabetical order*/
SELECT rv.name, r.mid, r.stars
FROM reviewer rv INNER JOIN rating r 
    ON rv.rid = r.rid
GROUP BY r.mid, rv.name, r.stars
ORDER BY r.mid ASC;

