import os
import json
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/<user_name>')
def hello_user(user_name):
    return f'Hello {user_name}'

@app.route('/index')
def index_page():
    return render_template('index.html')

@app.route('/movie/<movie_id>')
def show_movie_info(movie_id):
    movie = get_movie_info(movie_id)
    return render_template('movie.html', 
                    movie_title = movie['title'], 
                    movie_director = movie['director'],
                    movie_content = movie['content'])

def get_movie_info(movie_id):
    file_path = os.path.join(os.getcwd(), 'movie_data', f'{movie_id}.txt')
    movie_data = get_movie_data(file_path)
    return movie_data

def get_movie_data(file_path):
    try:
        with open(file_path, 'r') as f:
            json_data = json.load(f)
        return json_data
    except IOError:
        print(f'Unable to read file {file_path}')

# @app.route('/movies', method= ['GET', 'POST']):
# def get_movie_endpoint(end_point, movie_name):



#  if __name__ == '__main__':
#     flask.run(debug= True)