import json
import re

import db_slack


def insert2sql_users(user_token, db_connection, db_cursor):
    query = """ INSERT INTO Users (token) VALUES (%(user_token)s)
                RETURNING id; """
    db_cursor.execute(query, {"user_token" : user_token})
    # Retrive the insertion of user_id 
    db_connection.commit()
    user_id = db_cursor.fetchone()
    # print(f'inserted user_id : {user_id}')
    return user_id

def find_and_insert_uniq_users(users, thank_msg, db_connection, db_cursor):
    msg_user_token = thank_msg['user']
    if msg_user_token not in users.keys():
        msg_user_id = insert2sql_users(msg_user_token, db_connection, db_cursor)
        # Add a new user_token to users
        users[msg_user_token] = msg_user_id
        # Insert user from reactions
    if "reactions" in thank_msg.keys():
        for reaction in thank_msg['reactions']:
            for token in reaction['users']:
                if token not in users.keys():
                    user_id = insert2sql_users(token, db_connection, db_cursor)
                    users[token] = user_id 
    return users

def insert2sql_messages(user_id, msg, db_connection, db_cursor):
    query = """ INSERT INTO Messages (user_id, message, sent_at)
                VALUES (%(user_id)s, %(message_text)s, to_timestamp(%(ts)s))
                RETURNING id; """
    db_cursor.execute(query, {
        "user_id" : user_id,
        "message_text" : msg['text'],
        "ts" : msg['ts'].split('.')[0]
    })
    message_id = db_cursor.fetchone()
    # print(f'inserted message_id : {message_id}')
    return message_id

def insert2sql_reaction(message_id, users, reaction, db_connection, db_cursor):
    for user_token in reaction['users']:
        query = """ INSERT INTO Reactions (user_id, message_id, reaction)
                    VALUES (%(user_id)s, %(message_id)s, %(reaction_type)s) """
        db_cursor.execute(query, {
            "message_id" : message_id,
            "user_id" : users[user_token],
            "reaction_type" : reaction['name']
        })
        db_connection.commit()

def extra_mentioned_user(msg_text):
    regex = r'^<@([0-9a-zA-Z]{9})>?'


def process_json2sql(json_data, db_connection, db_cursor):
    """
    SQL Tables:
        - Message: id, user_id, channel, sent_at
        - Users: id, token, name
        - Reactions: id, user_id, message_id
        - Mentions: message_id, user_id
    """
    if not json_data:
        return
    user_col = ['user']
    message_col = ['client_msg_id', 'user', 'ts']
    reaction_col = ['client_msg_id', 'user']
    mention_col = ['user', 'client_msg_id']
    users = dict().fromkeys(['user_id', 'token'])
    for thank_msg in json_data:
        # Insert to database only when the user info and message id both exist. 
        if (user_col[0] in thank_msg.keys()) and (message_col[0] in thank_msg.keys()):
            msg_user_token = thank_msg['user']
            users = find_and_insert_uniq_users(users, thank_msg, db_connection, db_cursor)
            message_id = insert2sql_messages(users[msg_user_token], thank_msg, db_connection, db_cursor)
            # insert reactions
            if "reactions" in thank_msg.keys():
                for reaction in thank_msg['reactions']:
                    insert2sql_reaction(message_id, users, reaction, db_connection, db_cursor)
    # insert mentions
    print(f'inserted {len(users.keys())} user(s) and {message_id} message(s)')


json_data = db_slack.read_file('data', 'gfa-team-thanks.json')

user = {"a_user" : "postgres", "a_password" : "root"}
db_connection = db_slack.connect_to_db(user['a_user'], user['a_password'])
db_cursor = db_connection.cursor()
process_json2sql(json_data, db_connection, db_cursor)

