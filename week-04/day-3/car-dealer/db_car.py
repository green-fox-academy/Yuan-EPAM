import os
import json

import psycopg2

def get_file_path(file_name):
    return os.path.join(os.getcwd(), file_name)

def read_file(file_name):
    try:
        file_path = get_file_path(file_name)
        with open(file_path) as json_file:
            return json.load(json_file)
    except IOError as e:
        print(e)
        print(f'Unable to read file {file_path}')

def initial_db(a_user, a_password):
    try:
        connection = psycopg2.connect(
            user= a_user,
            password= a_password,
            host= '127.0.0.1',
            port= '5432',
            database= 'dsa'
        )
        cursor = connection.cursor()
        cursor.execute(open('car.sql', 'r').read())
        # print(connection.get_dsn_parameters(), "\n")
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print('Error while connecting to PostgresSQL', error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print('PostgreSQL connection is closed')

def connect_to_db(a_user, a_password):
    try:
        connection = psycopg2.connect(
            user= a_user,
            password= a_password,
            host= '127.0.0.1',
            port= '5432',
            database= 'dsa'
        )
        # print(connection.get_dsn_parameters(), "\n")
        print('PostgresSQL is connected')
        return connection
    except (Exception, psycopg2.Error) as error:
        print('Error while connecting to PostgresSQL', error)


# user = read_file('user-data.json')
# print(user)
# initial_db(user['user'], user['password'])
    
    

