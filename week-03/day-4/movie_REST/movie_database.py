import os
import json

# { 
    # "1" : "Godfather", 
    # "2": "Intouchable",
    #  "3": "The Dark Night",
    #  "4": "itness for the Prosecution",
    #  "5": "ock, Stock and Two Smoking Barrels"
# }

def get_movie_name_path():
    return  os.path.join(os.getcwd(), 'movie_data', 'movie_name.json')

def get_movie_path():
    return  os.path.join(os.getcwd(), 'movie_data', 'movie_sample.json')

def get_api_key_path():
    return os.path.join(os.getcwd(), 'token-key.txt')

def get_movie_name():
    movie_name_path = get_movie_name_path()
    try:
        with open(movie_name_path) as json_file:
            return json.load(json_file)
    except IOError:
        print(f'Unable to read file {movie_name_path}')

def create_new_movie_id():
    return str(len(init_movie_name) + 1)

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
                # print(data)
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

def write_movie_data(movie):
    movie_path = get_movie_path()
    try:
        with open(movie_path) as json_file:
            json_data = json.load(json_file)
            json_data.append(movie)
        with open(movie_path, 'w') as json_file:
            json.dump(json_data, json_file) 
    except IOError:
        print(f'Unable to read file {movie_path}')

def write_movie_name(movie):
    movie_name_path = get_movie_name_path()
    print(movie)
    try:
        with open(movie_name_path) as json_file:
            json_data = json.load(json_file)
            json_data.update({movie['id'] : movie['title']})
        with open(movie_name_path, 'w') as json_file:
            json.dump(json_data, json_file)
    except IOError as e:
        print(dir(e))
        print(f'Unable to read file {movie_name_path}')

def update_a_movie(new_movie):
    # init_movie_name[new_movie['id']] = new_movie['title']
    write_movie_data(new_movie)
    write_movie_name(new_movie)

init_movie_name = get_movie_name()
# print(read_api_key())
# print(init_movie_name)

# write_movie_name({ "id" : "7", "title" : "abc_test"})
# print(get_movie_name())