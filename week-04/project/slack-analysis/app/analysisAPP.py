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
        # if db_connection is None:
        db_connection = db_slack.connect_to_db('postgres', 'root', db_name) 
        return redirect(url_for('show_data'))
        return render_template('db.html')

"""
show data
"""
answer_query = {
    "most_msg" : """  SELECT u.id, u.token, COUNT(msg.id) AS msg_count
                FROM messages msg INNER JOIN users u
                    ON msg.user_id = u.id
                GROUP BY u.id, u.token
                ORDER BY msg_count DESC 
                LIMIT 8; """,
    "most_emoji" : """
                    SELECT reaction, COUNT(id) AS emoji_count 
                    FROM reactions
                    GROUP BY reaction
                    ORDER BY emoji_count DESC
                    LIMIT 8;
                    """,
    "most_reacted_user" : """ 
                    SELECT u.id, u.token AS user_token, COUNT(r.user_id) AS reaction_count
                    FROM reactions r INNER JOIN users u
                        ON r.user_id=u.id
                    GROUP BY u.id, u.token
                    ORDER BY reaction_count DESC
                    LIMIT 8;
                    """,
    "most_mentioned" : """ 
                    SELECT u.id, u.token, COUNT(m.user_id) AS mention_count
                    FROM mentions m INNER JOIN users u 
                        ON m.user_id=u.id
                    GROUP BY u.id, u.token
                    ORDER BY mention_count DESC
                    LIMIT 8;
                    """,
    "most_reaction_msg" : """ 
                    SELECT m.id AS message_id, COUNT(r.id) AS reaction_count
                    FROM messages m INNER JOIN reactions r 
                        ON m.id = r.message_id
                    GROUP BY m.id
                    ORDER BY reaction_count DESC
                    LIMIT 8;
                        """,
    "most_active_date" : """
                    SELECT DATE(sent_at) AS message_date, COUNT(m.id) AS message_active_count
                    FROM messages m
                    GROUP BY DATE(sent_at)
                    ORDER BY message_active_count DESC
                    LIMIT 8;"""
}

head_cols = {
    "most_msg" : ['User ID', 'User token', 'Message Sent Count'],
    "most_emoji" : ['Reaction Type', 'Emoji Count'],
    "most_reacted_user" : ['User ID', 'User Token', 'Reaction Count'],
    "most_mentioned" : ["User ID", "User Token", "Mentioned Count"],
    "most_reaction_msg" : ["Message ID", "Reaction Count"],
    "most_active_date" : ['Message Date', 'Message Active Count']
}

def get_data(query, db_cursor):
    db_cursor.execute(query)
    # TODO get the columns 
    print([x[0] for x in db_cursor.description])
    return db_cursor.fetchall()

@app.route('/yuan/message', methods=['GET', 'POST'])
def show_data():
    db_cursor = db_connection.cursor()
    if request.method == 'POST':
        submit_val = request.form['load_data']
        print(f'submit_val: {submit_val}')
        if submit_val in answer_query.keys():
            res = get_data(answer_query[submit_val], db_cursor)
            heads = head_cols[submit_val]
            return render_template('db.html', res = res, heads = heads)
    return render_template('db.html')




