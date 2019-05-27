/*
List the users who registered in 2018 
with a .com email address and living in China
*/
SELECT *
FROM users
WHERE EXTRACT(YEAR FROM date_of_registration) = 2018
    AND email LIKE '%@%.com'
    AND country = 'China';


/* How many users are there?  100*/
SELECT DISTINCT COUNT(id)
FROM users


/* How many users registered in 2019?  42*/
SELECT DISTINCT COUNT(id)
FROM users 
WHERE EXTRACT(YEAR FROM date_of_registration) = 2019


/* How many users registered in January? 4 */
SELECT DISTINCT COUNT(id)
FROM users
WHERE EXTRACT(MONTH FROM date_of_registration)=1


/* Which country has the most users  China 17*/
SELECT DISTINCT COUNT(id) as User_Count, country
FROM users
GROUP BY country
ORDER BY User_Count DESC
LIMIT 1 


/* What is the gender ratio? 40:55 (male : female)*/
SELECT DISTINCT COUNT(id), gender
FROM users
WHERE gender IS NOT NULL
GROUP BY gender

/* How many users left at least one field blank? 11 */
SELECT DISTINCT COUNT(id)
FROM users
WHERE username IS NULL
    OR email IS NULL
    OR date_of_registration IS NULL
    OR first_name IS NULL
    OR last_name IS NULL
    OR country IS NULL
    or gender IS NULL


/* Which are the 3 most expensive products */
SELECT *
FROM products
ORDER BY price DESC
LIMIT 3


/* Which are the 4th and 5th cheapest products? */
SELECT *
FROM products
ORDER BY price
LIMIT 2 OFFSET 3


/* What is the average price for an electric product? */
SELECT DISTINCT AVG(id) AS AVG_Electronic
FROM products 
WHERE category='Electronics'


/* How much could it cost me to buy all the toys */
SELECT DISTINCT SUM(id) AS Total_Value_Toys
FROM products
WHERE category='Toys'


/* What is the average rating? */
SELECT AVG(rating) AS AVG_rating
FROM reviews


/* Which product has the best average rating? */
SELECT p.id, p.category, r.rating
FROM products p INNER JOIN reviews r 
    ON p.id = r.product_id
ORDER BY r.rating DESC
LIMIT 1


/* Which product has the worst rating? */
SELECT p.id, p.category, r.rating
FROM products p INNER JOIN reviews r 
    ON p.id = r.product_id
ORDER BY r.rating 
LIMIT 1


/* Which products have no review? */
SELECT p.id, p.category, r.comment
FROM products p LEFT JOIN reviews r
    ON p.id = r.product_id
WHERE r.comment IS NULL


/* How many reivews are 3 or below without comment? */
SELECT p.id, count(comment) AS less_3_comment
FROM products p LEFT JOIN reviews r
    ON p.id = r.product_id
GROUP BY p.id
HAVING COUNT(comment) < 3;


/* Which user reviewed the most? */
SELECT u.id, u.username, COUNT(comment) AS user_comment_number
FROM users u INNER JOIN reviews r
    ON u.id = r.user_id
GROUP BY u.id, u.username
ORDER BY COUNT(comment) DESC
LIMIT 1;


/* List the average rating for each product */
SELECT p.category, AVG(r.rating) AS AVG_rating
FROM products p INNER JOIN reviews r
    ON p.id = r.product_id
GROUP BY p.category;


/* How many days passed since the last review? 3 */
SELECT DATE_PART('day', NOW() - date) AS day_interval
FROM reviews
ORDER BY day_interval
LIMIT 1;

-- SELECT date, NOW()
-- FROM reviews
-- ORDER BY date DESC;

