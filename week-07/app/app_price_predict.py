import os 
import sys
sys.path.append('..')
sys.path.append('../db')
sys.path.append('../Model')
import pickle
import base64
from io import BytesIO

from flask import Flask, render_template, url_for, redirect
from flask import request
from flask_bootstrap import Bootstrap

import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import mplleaflet
import IPython


from db_psql import DBPsql
from ml import ML

app = Flask(__name__)
bootstrap = Bootstrap(app)

db_psql = DBPsql()
db_psql.connect()
ml = ML(db_psql)
# ml.close_db_connection()

@app.route('/')
def index():
    return render_template('index.html')

def load_model(db):
    try:
        query = """ SELECT clf FROM Model WHERE id = 1 """
        db_psql.cursor.execute(query)
        clf_obj = db_psql.cursor.fetchone()[0]
        return pickle.loads(clf_obj)
    except Exception as e:
        print(e)

def predict_price(value):
    target = pd.DataFrame({"bedroom_num" : np.array([value])})
    print(f'target {target}')
    clf = load_model(db_psql)
    print(type(clf))
    print(clf.predict([[1]]))
    return clf.predict(target)

def load_ml_data():
    ml.connect2db()
    ml.join_tables()
    ml.preprocessing_data()

def test_plot_leaflet(location= ''):
    lon = -84.0156
    lat = 41.9164
    plt.figure(figsize= (10, 10))
    # print(ml.data['latitude'][:10])
    # print(ml.data['longitude'][:10])
    plt.scatter(ml.data['longitude'][:600], ml.data['latitude'][:600], c= 'r', alpha= 0.7, s =1)
    # plt.hist2d(ml.data['longitude'][:100], ml.data['latitude'][:100], 
                # bins= 50)
    # plt.scatter(lon, lat, c= 'r', alpha= 0.7, s =5)
    # img_to_save = os.path.join(os.getcwd(), 'static', 'test1.png')
    # fig.savefig(img_to_save, format= 'png')
    # encoded = base64.b64encode(tmpfile.getvalue())
    return mplleaflet.display()

def load_location(location):
    location_dict = {"Bath and North East Somerset" : 0, "Devon" : 0, "Dorset" :0,
            	"North Somerset" :0, "Somerset" :0, "Vale of Glamorgan" :0}
    if location in location_dict.keys():
        return location_dict.update({location : 1})

@app.route('/', methods=['GET', 'POST'])
def show_prediction():
    load_ml_data()
    if request.method == 'POST':
        submit_val = request.form['bedroom_num']
        print(f'-->submit_val: {submit_val}')
        price_predicted = round(predict_price(submit_val).tolist()[0], 2)
        test_map = test_plot_leaflet()
    return render_template('index.html', recommendation_price= price_predicted,
                                        test_map = test_map)


