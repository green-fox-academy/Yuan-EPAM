import os
import json

import psycopg2

class DBPsql:
    def __init__(self, user= 'postgres', password= 'root', db_name= 'real_estate'):
        self._user = user
        self._password = password
        self._db_name = db_name
        self._connection = None
        self._cursor = None

    def initialize(self, db_init_file):
        try:
            init_file_path = os.path.abspath(db_init_file)
            self._connection = psycopg2.connect(
                user = self._user,
                password = self._password,
                host = '127.0.0.1',
                port = '5432',
                database = self._db_name
            )
            self._cursor = self._connection.cursor()
            self._cursor.execute(open(init_file_path, 'r').read())
            self._connection.commit()
            print(f'DataBase: {self._db_name} initialized.')
        except (Exception, psycopg2.Error) as e:
            print('Error while connecting to PostgreSQL', e)
        finally:
            if self._connection:
                self._cursor.close()
                self._connection.close()
                print('PostgreSQL connection is closed.')
    
    def connect(self):
        try:
            self._connection = psycopg2.connect(
                user = self._user,
                password = self._password,
                host = '127.0.0.1',
                port = '5432',
                database = self._db_name
            )
            self._cursor = self._connection.cursor()
            print('PostgreSQL is connected')
        except (Exception, psycopg2.Error) as e:
            print('Error while connecting to PostgreSQL', e)

    def close(self):
        if self._connection:
            self._cursor.close()
            self._connection.close()
            print('PostgreSQL connection is closed')

    @property
    def cursor(self):
        return self._cursor
    
    @property
    def connection(self):
        return self._connection


# TODO store user file in database
# user = 'postgres'
# password = 'root'
# db_name = 'real_estate'
# db_psql = DBPsql()
# db_psql.initialize(db_init_file= 'db_ml_model.sql')
# db_psql.connect()
# db_psql.close()
# print(db_psql.connection.status)
# db_psql.connect()