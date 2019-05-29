import db_todoAPP
import command_line

def list_task(db_cursor):
    query = """ SELECT * FROM Task """
    db_cursor.execute(query)
    print(db_cursor.fetchall())
    # return query

def add_task(new_task, db_connection, db_cursor):
    query = """ INSERT INTO Task (description) VALUES (%(new_task)s) """
    db_cursor.execute(query, {"new_task": new_task})
    db_connection.commit()
    # list_task(db_cursor)

def remove_task(taskID_to_rm, db_connection, db_cursor):
    query = """ DELETE FROM Task WHERE tId=(%(task_ID)s) """
    db_cursor.execute(query, {"task_ID": taskID_to_rm})
    db_connection.commit()

def process_command_line(options, db_connection, db_cursor):
    print(options)
    if options.add:
        add_task(options.add, db_connection, db_cursor)
        print('Added a task')
    if options.remove:
        remove_task(options.remove, db_connection, db_cursor)
        print('removed a task')
    else:
        if options.list:
            list_task(db_cursor)
            print('list all tasks')


""" 
connect to database by using default 
"""
user = db_todoAPP.get_user()
db_connection = db_todoAPP.connect_to_db(user['user'], user['password'])
db_cursor = db_connection.cursor()

# list_task(db_cursor)

"""
process command line argument
"""
(options, args) = command_line.initial_command_options()
process_command_line(options, db_connection, db_cursor)


"""
Close database connection
"""
if db_connection:
    db_cursor.close()
    db_connection.close()
    print('PostgresSQL connection is closed')