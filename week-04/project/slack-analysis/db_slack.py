import os
import json

import psycopg2

def get_file_path(folder, file_name):
    return os.path.join(os.getcwd(), folder, file_name)

def read_file(folder, file_name):
    file_path = get_file_path(folder, file_name)
    try:
        with open(file_path) as json_file:
            return json.load(json_file)
    except IOError as e:
        print(e)
        print(f'Unable to read file {file_path}')

def initialize_db(a_user, a_password):
    try:
        db_file_path = get_file_path('db', 'db_slack.sql')
        connection = psycopg2.connect(
            user = a_user,
            password = a_password,
            host = '127.0.0.1',
            port = '5432',
            database = 'slack_analysis'
        )
        cursor = connection.cursor()
        cursor.execute(open(db_file_path, 'r').read())
        connection.commit()
        print('Initialized db')
    except (Exception, psycopg2.Error) as e:
        print('Error while connecting to PostgresSQL', e)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('PostgresSQL connection is closed')

def connect_to_db(a_user, a_password):
    try:
        connection = psycopg2.connect(
            user = a_user,
            password = a_password,
            host = '127.0.0.1',
            port = '5432',
            database = 'slack_analysis'
        )
        print('PostgresSQL is connected')
        return connection
    except (Exception, psycopg2.Error) as e:
        print('Error while connecting to PostgresSQL', e)

user = {"a_user" : "postgres", "a_password" : "root"}
initialize_db(user['a_user'], user['a_password'])