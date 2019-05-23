import os
import json

init_movie_name = {
    "1" : "Godfather",
    "2": "Intouchable",
    "3": "The Dark Night",
    "4": "itness for the Prosecution",
    "5": "ock, Stock and Two Smoking Barrels"
}

def get_file_path():
    return  os.path.join(os.getcwd(), 'movie_data', 'movie_sample.txt')

def read_all_movie_data():
    file_path = get_file_path()
    try:
        with open(file_path) as json_file:
            return json.load(json_file)
    except IOError:
        print(f'Unable to read file {file_path}')

def read_movie_data(movie_id):
    file_path = get_file_path()
    try:
        with open(file_path) as json_file:
            json_data = json.load(json_file)
            for data in json_data:
                if data['id'] == str(movie_id):
                    return data
    except IOError:
        print(f'Unable to read file {file_path}')

# print(read_movie_data(1))
    