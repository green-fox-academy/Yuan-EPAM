import sys
sys.path.append('..')

from flask import Flask, render_template, url_for, redirect
from flask import request
from flask_bootstrap import Bootstrap

import db_slack

app = Flask(__name__)

bootstrap = Bootstrap(app) 

# global variable TODO db --> OOP and to use session
db_connection = None

@app.route('/')
def index():
    return redirect(url_for('user'))

@app.route('/yuan')
def user():
    return render_template('index.html')

"""
connect to slack_analysis database
"""
@app.route('/yuan/db', methods=['GET', 'POST'])
def connect_db():
    if request.method == 'POST':
        print(request.form['db'])
        global db_connection
        db_name = request.form['db']
        if db_connection is None:
            db_connection = db_slack.connect_to_db('postgres', 'root', db_name) 
        return redirect(url_for('show_data'))
        return render_template('db.html')

"""
show data
"""
answer_query = {
    "most_msg" : """  SELECT u.token, COUNT(msg.id) AS msg_count
                FROM messages msg INNER JOIN users u
                    ON msg.user_id = u.id
                GROUP BY u.token
                ORDER BY msg_count DESC 
                LIMIT 1; """
}

def get_most_msg(query, db_cursor):
    db_cursor.execute(query)
    return db_cursor.fetchall()

def get_most_common_emoji(db_cursor):
    query = """ """

@app.route('/yuan/message', methods=['GET', 'POST'])
def show_data():
    # query = """ SELECT * FROM users LIMIT 5 """
    db_cursor = db_connection.cursor()
    res_1 = get_most_msg(answer_query['most_msg'], db_cursor)
    print(res_1)
    return render_template('db.html', res_1 = res_1)


