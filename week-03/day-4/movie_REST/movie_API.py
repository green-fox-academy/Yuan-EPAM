import os
from flask import Flask, render_template, redirect, url_for
from flask import request, jsonify

import get_movie_data as movie_db

app = Flask(__name__)

@app.route('/')
def home_page():
    return redirect('api')

@app.route('/api')
def show_home_page():
    if not movie_db.init_movie_name:
        return render_template('index.html', init_movie_name = {"1": "<---No Movie Here--->"})
    else:
        return render_template('index.html', init_movie_name = movie_db.init_movie_name)

def get_API_data(movie_id= None):
    # print(f'request method: {request.method}')
    if not movie_id:
        movie_data = movie_db.read_all_movie_data()
    else:
        movie_data = movie_db.read_movie_data(movie_id)
    return jsonify(movie_data)

@app.route('/api/movies', methods= ['GET'])
def show_all_movie_data():
    print(f'show all movie data')
    if request.method == 'GET':
        response_movies = get_API_data()
        response_movies.status_code = 200
        return response_movies
    # return render_template('api_response.html', api_response = response_movies)

@app.route('/api/movies/<movie_id>', methods= ['GET'])
def show_movie_data(movie_id):
    print(f'movie_id {movie_id}')
    if request.method == 'GET':
        response_movie = get_API_data(movie_id)
        print('response_movie:')
        print(response_movie)
        response_movie.status_code = 200
        return response_movie