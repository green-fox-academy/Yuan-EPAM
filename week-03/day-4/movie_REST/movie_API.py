import os
from flask import Flask, render_template, redirect, url_for
from flask import request, jsonify

import movie_database as movie_db

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

"""
---------------- GET ---------------- 
"""
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
        response_movie.status_code = 200
        return response_movie

def check_api_key(api_key_user):
    return api_key_user == movie_db.get_api_key()

def create_movie():
    movie_id = None
    if request.form['movie_id'] in movie_db.init_movie_name.keys():
        movie_id = request.form['movie_id']
    else:
        movie_id = movie_db.create_new_movie_id()
    return {
        'id' : movie_id,
        'title' : request.form['title'],
        'year' : request.form['genre'],
        'description' : request.form['description']
    }


"""
---------------- POST ---------------- 
"""
def add_new_movie():
    new_movie = create_movie()  
    resp_new_movie = jsonify(new_movie)
    resp_new_movie.status_code = 200
    movie_db.update_a_movie(new_movie)
    return resp_new_movie

"""
---------------- PUT ---------------- 
"""
def modify_movie():
    movie_id = request.form['movie_id']
    print(f'movie_id {movie_id}')
    if movie_id in movie_db.init_movie_name.keys():
        # TODO to see if it really could be used for add and modify functions
        return add_new_movie()
    else:
        failed = jsonify({"error" : f"No movie found with {movie_id} ID"})
        failed.status_code = 404
        return failed

@app.route('/api/movies', methods= ['GET', 'POST'])
def manipulate_movie():
    if request.method == 'POST':
        api_key = request.form['api-key']
        # print(f'request.form {request.form}')
        if check_api_key(api_key):
            if request.form['update_movie'] == 'add':
                return add_new_movie()
            elif request.form['update_movie'] == 'modify':
                return modify_movie()
        else:
            failed = jsonify({"error" : "Invalid API_KEY"})
            failed.status_code = 403
            return failed

"""
---------------- DELETE ---------------- 
"""
@app.route('/api/movies/', methods= ['GET', 'POST'])
def delete_movie():
    if request.method == 'POST':
        api_key = request.form['api-key']
        if check_api_key(api_key):
            movie_id = request.form['movie_id']
            if movie_id in movie_db.init_movie_name.keys():
                print(f'movie_id {movie_id}')
                movie_db.delete_a_movie(movie_id)
                return redirect(f"/api/movies/{movie_id}")
            else:
                failed = jsonify({"error" : f"No movie found with {request.form['movie_id']} ID"})
                failed.status_code = 404
                return failed
        else:
            failed = jsonify({"error" : "Invalid API_KEY"})
            failed.status_code = 403
            return failed
