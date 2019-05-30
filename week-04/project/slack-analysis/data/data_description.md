### _thanks channel history

| Feature           | Description                                                  |      |
| ----------------- | ------------------------------------------------------------ | ---- |
| client_msg_id     | message identifier                                           |      |
| type              | type `"message"` are user entered text messages sent to the channel, while other types are `events` that happened within the channel. (message only?) |      |
| text              | mentioned people (optional and need to be extracted) + content |      |
| user              | the user ID created the thank message                        |      |
| ts                | timestamp of this thank message created                      |      |
| edited            | message was edited                                           |      |
| edited (user)     | the user edited the message                                  |      |
| edited (ts)       | timestamp of the edited                                      |      |
| thread_ts         | equal to the top ts message                                  |      |
| reply_count       |                                                              |      |
| reply_users_count |                                                              |      |
| reply_users       |                                                              |      |
| replies           |                                                              |      |
| replies (user)    | a user                                                       |      |
| replies (ts)      | the timestamp                                                |      |
| subscribed        |                                                              |      |
| reactions         | contains any reactions that have been added to               |      |
| reactions(name)   | the type of reaction                                         |      |
| reactions(users)  | a list `(possibly incomplete)` of users who have added that reaction to the message. But all the users are guaranteed to appear in the `users` array. |      |
| reactions(count)  | always represent the count of all users who made that reaction (it may be greater than `users.length`) |      |
|                   |                                                              |      |
|                   |                                                              |      |

#### Q:

- Where does the `channel` data hide?

  A: json file name (like `gfa-team-thanks` channel, `gfa-team-thanks-replies` channel)

