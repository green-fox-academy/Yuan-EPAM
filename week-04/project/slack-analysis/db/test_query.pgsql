SELECT *
FROM users;

SELECT *
FROM messages;

SELECT DATE(sent_at)
FROM messages;

SELECT *
FROM Reactions;

SELECT DISTINCT user_id
FROM mentions;

-- SELECT msg.id as msg_id, u.token, u.id AS user_id
-- FROM messages msg INNER JOIN users u
    -- ON msg.user_id = u.id
-- WHERE u.token = 'U0AA4Q8LS';

/* ----------------------- Thanks Channel ----------------------- */
/* 1. Who sent the most messages to the thanks channel? */
SELECT u.id, u.token, COUNT(msg.id) AS message_count
FROM messages msg INNER JOIN users u
    ON msg.user_id = u.id
GROUP BY u.id, u.token
ORDER BY message_count DESC
LIMIT 1;

/* 2. Which emoji is the most common as reaction in the thanks channel? */
SELECT reaction, COUNT(id) AS emoji_count
FROM reactions
GROUP BY reaction
ORDER BY emoji_count DESC
LIMIT 1;

/* 3. Who reacted to most messages? */
SELECT u.id, u.token AS user_token, COUNT(r.user_id) AS reaction_count
FROM reactions r INNER JOIN users u
    ON r.user_id=u.id
GROUP BY u.id, u.token
ORDER BY reaction_count DESC
LIMIT 1;

/* 4. Who is the most mentioned person in the thanks channel */
SELECT u.id, u.token, COUNT(m.user_id) AS mention_count
FROM mentions m INNER JOIN users u 
    ON m.user_id=u.id
GROUP BY u.id, u.token
ORDER BY mention_count DESC
LIMIT 1;

/* 5. Which message got the most reactions in the thanks channel */
SELECT m.id AS message_id, COUNT(r.id) AS reaction_count
FROM messages m INNER JOIN reactions r 
    ON m.id = r.message_id
GROUP BY m.id
ORDER BY reaction_count DESC
LIMIT 1;

/* 6. Which day was the most active in the channel? */
SELECT DATE(sent_at) AS message_date, COUNT(m.id) AS message_active_count
FROM messages m
GROUP BY DATE(sent_at)
ORDER BY message_active_count DESC;





 