import datetime

import db_car
import command_line

def convert_json2sql(json_data, db_connection, db_cursor):
    if not json_data:
        return 
    cols = ['brand', 'model', 'year', 'condition', 'price', 'count']
    query = """ INSERT INTO Car (brand, model, year, condition, price, count) 
                    VALUES (%(car_brand)s, %(car_model)s, %(car_year)s, 
                            %(car_condition)s, %(car_price)s, %(car_count)s)"""
    for car in json_data:
        db_cursor.execute(query, {
            "car_brand" : car[cols[0]],
            "car_model" : car[cols[1]],
            "car_year" : car[cols[2]],
            "car_condition" : car[cols[3]],
            "car_price" : car[cols[4]],
            "car_count" : car[cols[5]]
        })
        db_connection.commit()

def remove_num_stock(num, db_connection, db_cursor):
    query = """ DELETE FROM Car WHERE count=%(store_num)s; """
    db_cursor.execute(query, {"store_num": num})
    db_connection.commit()

def decrease_price(car_condition, db_connection, db_cursor):
    query = """ UPDATE Car SET price = price * 0.8 
                WHERE condition=%(car_condition)s; """
    db_cursor.execute(query, {"car_condition" : car_condition})
    db_connection.commit()

def count_avg_aging(cur_year, db_connection, db_cursor):
    query = """ SELECT ROUND(AVG(age.car_age), 2) AS avg_car_age
                FROM (SELECT (%(cur_year)s - year) AS car_age
                      FROM car
                      WHERE count != 0) AS age; """
    db_cursor.execute(query, {"cur_year": cur_year})
    print(db_cursor.fetchall())
    db_connection.commit()

def process_command_line(options, db_connection, db_cursor):
    # print(options)
    if options.remove != None:
        remove_num_stock(options.remove, db_connection, db_cursor)
        print(f'removed car with {options.remove} store')
    if options.decrease:
        decrease_price(options.decrease, db_connection, db_cursor)
        print(f'Decreased the price of {options.decrease} by 20%')
    if options.average:
        count_avg_aging(options.average, db_connection, db_cursor)

user = db_car.read_file('user-data.json')
"""
Initialization database (It should be executed only one time)
"""
db_car.initial_db(user['user'], user['password'])


"""
Connect to database
"""
db_connection = db_car.connect_to_db(user['user'], user['password'])
db_cursor = db_connection.cursor()


"""
Convert json data to PostgresSQL

"""
json_data = db_car.read_file('cars.txt')
convert_json2sql(json_data, db_connection, db_cursor)


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