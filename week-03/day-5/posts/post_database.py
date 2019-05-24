import os
import json

def get_file_path(file_name):
    return os.path.join(os.getcwd(), file_name)

def get_file_data(file_name):
    file_path = get_file_path(file_name)
    try:
        with open(file_path) as json_file:
            return json.load(json_file)
    except IOError as e:
        print(e)
        print(f'Unable to read file {file_path}')


# print(get_file_data('posts.json'))