import os
import json

init_movie_name = {
    "1" : "Godfather",
    "2": "Intouchable",
    "3": "The Dark Night",
    "4": "itness for the Prosecution",
    "5": "ock, Stock and Two Smoking Barrels"
}

def get_movie_path():
    return  os.path.join(os.getcwd(), 'movie_data', 'movie_sample.txt')

def get_api_key_path():
    return os.path.join(os.getcwd(), 'token-key.txt')

def create_new_movie_id():
    return len(init_movie_name) + 1

def read_all_movie_data():
    file_path = get_movie_path()
    try:
        with open(file_path) as json_file:
            return json.load(json_file)
    except IOError:
        print(f'Unable to read file {file_path}')

def read_movie_data(movie_id):
    file_path = get_movie_path()
    try:
        with open(file_path) as json_file:
            json_data = json.load(json_file)
            for data in json_data:
                if data['id'] == str(movie_id):
                    return data
    except IOError:
        print(f'Unable to read file {file_path}')

def get_api_key():
    api_key_path = get_api_key_path()
    try:
        with open(api_key_path) as key_file:
            res = []
            for line in key_file:
                res.append(line)
            return ''.join(res)
    except IOError:
        print(f'Unable to read file {api_key_path}')

# print(read_api_key())
