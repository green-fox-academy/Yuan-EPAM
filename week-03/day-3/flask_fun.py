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
    return render_template('movies.html', 
                    movie_title = movie['title'], 
                    movie_director = movie['director'],
                    movie_content = movie['content'])

def get_movie_info(movie_id):
    movie_info = {
        '1': {
            'title': 'Godfather',
            'director': 'Directors of Godfather',
            'content': 'Content of Godfather'
        },
        '2': {
            'title': 'Intouchable',
            'director': 'Directors of Intouchable',
            'content': 'Content of Intouchable'
        },
        '3': {
            'title': 'The Dark Night',
            'director': 'Directors of The Dark Night',
            'content': 'Content of The Dark Night'
        },
        '4': {
            'title': 'Witness for the Prosecution',
            'director': 'Directors of Witness for the Prosecution',
            'content': 'Content of Witness for the Prosecution'
        },
        '5': {
            'title': 'Lock, Stock and Two Smoking Barrels',
            'director': 'Director of Lock, Stock and Two Smoking Barrels',
            'content': 'Content of Lock, Stock and Two Smoking Barrels'
        }
    }
    return movie_info[movie_id]

# @app.route('/movies', method= ['GET', 'POST']):
# def get_movie_endpoint(end_point, movie_name):



#  if __name__ == '__main__':
#     flask.run(debug= True)