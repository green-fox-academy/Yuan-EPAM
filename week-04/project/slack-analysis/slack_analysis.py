import db_slack
import process_data 
import cml

def cml_init_db(user, db_name):
    db_slack.initialize_db(user['a_user'], user['a_password'], db_name)

def cml_add_data(file_name, user):
    # Load json data
    json_data = db_slack.read_file('data', file_name)
    # Connect to database
    db_connection = db_slack.connect_to_db(user['a_user'], user['a_password'])
    db_cursor = db_connection.cursor()
    # Convert json data and store them in database
    process_data.convert_json2sql(json_data, db_connection, db_cursor)
    if db_connection:
        db_cursor.close()
        db_connection.close()
        print('PostgresSQL connection is closed')

def drive_cml(user):
    (options, args) = cml.initialize_command_options()
    if options.init_db:
        cml_init_db(user, options.init_db)
    if options.add_json:
        file_name = options.add_json
        cml_add_data(file_name, user)
        print(f'Loaded file "{file_name}" to database!')

# TODO user info input from web
user = {"a_user" : "postgres", "a_password" : "root"}

""" 
file name:
 - gfa-team-thanks.json
 - gfa-team-random.json
 - gfa-team-thanks-replies.json
"""
drive_cml(user)
