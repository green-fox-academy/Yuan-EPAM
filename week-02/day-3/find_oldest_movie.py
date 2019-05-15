import os

def use_rel_path(file_path):
    return os.getcwd(file_path)  


def read_file(file_path):
    try:
        res = []
        with open(file_path) as f:
            for line in f:
                res.append(line)
        return ''.join(res)
    except IOError:
        print(f'Unable to read file {file_path}')


print(use_rel_path('movies.txt'))

# def find_oldest_movie(file_path):
# file_path = os.path.relpath('./movies.txt')
# read_file(file_path)


