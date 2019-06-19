import sys
sys.path.append('.')
sys.path.append('..')

import os
import json
import re

import psycopg2

from db_psql import DBPsql

class JSONtoDB:
    def __init__(self, db):
        self._db = db
        self._data = None
        self._data_source = None
        self._data_res = None
        self._data_lists = None
        self._house = {}
        self._house_location = {}
        self._price = {}
        self._lister = {}

    def get_data_folder(self, folder= 'json'):
        return os.path.join(os.getcwd(), 'API', 'data', folder)

    def find_json_data(self):
        p = r'[0-9]{1,4}api_nestoria\.json'
        regex = re.compile(p)
        folder = self.get_data_folder()
        files = os.listdir(folder)
        res = []
        for f in files:
            if regex.match(f):
                file_path = os.path.join(folder, regex.match(f)[0])
                res.append(file_path)
        # print(res)
        return res

    def load_data(self, file_path):
        try:
            with open(file_path) as f:
                print(f'reading {file_path}')
                self._data = json.load(f)
        except Exception as e:
            print(f'Uable to read file {file_path}', e)

    def insert2sql_house(self, *args, **kwargs):
        """
        House Table Columns:
            id (PK), type (varchar), bedroom_number (INT), bathroom_number (INT),
            car_spaces (INT), keywords (TEXT), title (TEXT), summary (TEXT)
        """
        query = """ INSERT INTO House (type, bedroom_num, bathroom_num,
                           car_spaces, keywords, title, summary) 
                    VALUES (%(type)s, %(bedroom_num)s, %(bathroom_num)s,
                            %(car_spaces)s, %(keywords)s, %(title)s, %(summary)s)
                    RETURNING id; """
        query_values = {"type" : None, "bedroom_num" : None, "bathroom_num" : None,
                       "car_spaces" : None, "keywords" : None, "title" : None, "summary" : None}
        query_values.update(*args, **kwargs)
        self._db.cursor.execute(query, query_values)
        self._db.connection.commit()
        house_id = self._db.cursor.fetchone()
        return house_id
    
    def insert2sql_location(self, *args, **kwargs):
        """
        Location Table Columns:
            id (PK), house_id (fk), latitude (float), longitude (float), location_accuracy (float),
            country (TEXT), city (TEXT), town (TEXT), area (TEXT), street (TEXT)
        """
        query = """ INSERT INTO HouseLocation (house_id, latitude, longitude, location_accuracy,
                           location, country, city, town, area, street)
                    VALUES (%(house_id)s, %(latitude)s, %(longitude)s, %(location_accuracy)s,
                            %(location)s, %(country)s, %(city)s, %(town)s, %(area)s, %(street)s); """
        query_values = {"house_id" : None, "latitude" : None, "longitude" : None, "location_accuracy" : None,
                        "location" : None, "country" : None, "city" : None, "town" : None, "area" : None, "street" : None}
        query_values.update(*args, **kwargs)
        self._db.cursor.execute(query, query_values)
        self._db.connection.commit()

    def insert2sql_price(self, *args, **kwargs):
        """
        Price Table Columns:
            id (pk), house_id (fk), price (float), price_currency (text),
            price_high (float), price_low (float), price_type (varchar)
        """
        query = """ INSERT INTO Price (house_id, price, price_currency,
                                       price_high, price_low, price_type)
                    VALUES (%(house_id)s, %(price)s, %(price_currency)s,
                            %(price_high)s, %(price_low)s, %(price_type)s)
                    RETURNING id; """
        query_values = {"house_id" : None, "price" : None, "price_currency" : None, 
                        "price_high" : None, "price_low" : None, "price_type" : None}
        query_values.update(*args, **kwargs)
        self._db.cursor.execute(query, query_values)
        self._db.connection.commit()
        price_id = self._db.cursor.fetchone()
        return price_id

    def insert2sql_lister(self, *args, **kwargs):
        """
        Lister Table Columns:
            id (pk), name (TEXT), house_id (fk), price_id (fk), list_type, post_time (timestamp)
        """
        query = """ INSERT INTO Lister (name, house_id, price_id, list_type, post_time)
                    VALUES (%(name)s, %(house_id)s, %(price_id)s, %(list_type)s, %(post_time)s)
                    RETURNING id """
        query_values = {"name" : None, "house_id" : None, "price_id" : None, "list_type" : None, "post_time" : None}
        query_values.update(*args, **kwargs)
        self._db.cursor.execute(query, query_values)
        self._db.connection.commit()
        lister_id = self._db.cursor.fetchone()
        return lister_id

    def load_house(self, item):
        cols = {"property_type" : "type", "bedroom_number" : "bedroom_num", 
                "bathroom_number" : "bathroom_num", "car_spaces" : "car_spaces", "keywords" : "keywords",
                 "title" : "title", "summary" : "summary"}
        for key in cols.keys():
            if key in item.keys():
                self._house[cols[key]] = item[key]

    def load_house_location(self, house_id, item, data_source):
        cols = {"latitude" : "latitude", "longitude" : "longitude", "location_accuracy" : "location_accuracy",
                "location" : "location"}
        for key in cols.keys():
            if key in item.keys():
                self._lister[cols[key]] = item[key]
        self._house_location.update({
            "house_id" : house_id, "location" : data_source['location'], 
            "country" : data_source['country'], "city" : None, "town" : None, "area" : None, "street" : None
        })

    def load_price(self, house_id, item):
        cols = {"price" : "price", "price_currency" : "price_currency", "price_high" : "price_high",
                "price_low" : "price_low", "price_type" : "price_type"}
        for key in cols.keys():
            if key in item.keys():
                self._price[cols[key]] = item[key]
        self._price.update({ "house_id" : house_id})

    def load_lister(self, house_id, price_id, item, data_res):
        cols = {"lister_name" : "name", "listing_type" : "list_type", "created_unix" : "post_time"}
        for key in cols.keys():
            if key in item.keys():
                self._lister[cols[key]] = item[key]
        self._lister.update({
            "house_id" : house_id, "price_id" : price_id,
             "post_time" : data_res['created_unix']
        })

    def start(self):
        # TODO convert json data to db during requesting api
        files = self.find_json_data()
        for file in files:
            self.load_data(file)
            if self._data:
                self._data_source = self._data['request']
                self._data_res = self._data['response']
                self._data_lists = self._data_res['listings']
                for item in self._data_lists:
                    self.load_house(item)
                    house_id = self.insert2sql_house(self._house)
                    self.load_price(house_id, item)
                    price_id = self.insert2sql_price(self._price)

                    self.load_house_location(house_id, item, self._data_source )
                    self.load_lister(house_id, price_id, item, self._data_res)
                    self.insert2sql_location(self._house_location)
                    self.insert2sql_lister(self._lister)


# user = 'postgres'
# password = 'root'
# db_name = 'real_estate'
# db_psql = DBPsql(user, password, db_name)
# db_psql.initialize(folder= 'db', db_init_file= 'db_real_estate.sql')
# db_psql.connect()

# test_insert = {
#     "type" : "flat",
#     "bathroom_number" : None,
#     "car_spaces" : None,
#     "status" : "buy",
#     "bedroom_number" : 1,
#     "keywords" : "test house flat",
#     "summary" : "good to buy"
# }
# json2db = JSONtoDB(db_psql)
# json2db.insert2sql_house(test_insert)
# print(json2db.get_data_folder())
# json2db.find_json_data()
# json2db.start()