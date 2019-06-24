import os
import sys
sys.path.append('..')
sys.path.append(os.path.join('..', 'db'))

import numpy as np 
import pandas as pd  
from pandas.io.json import json_normalize
import matplotlib.pyplot as pyplot

from sklearn import preprocessing
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
import joblib 
import pickle

import reverse_geocoder as rg

from db_psql import DBPsql

class ML:
    def __init__(self, db):
        self._db = db
        self._df = pd.DataFrame()
        self._df_train = None
        self._features = None
        self._target = None
        self._X_train = None
        self._X_test = None
        self._Y_train = None
        self._Y_test = None
        self._clf = None

    def connect2db(self):
        self._db.connect()

    def close_db_connection(self):
        if self._db.connection:
            self._db.cursor.close()
            self._db.connection.close()
            print('DB connection is closed')
    
    def read_sql_table(self, table_name):
        query = f"SELECT * FROM {table_name}"
        df = pd.DataFrame()
        for chunk in  pd.read_sql_query(query, self._db.connection, chunksize= 5000):
            df = pd.concat([df, chunk], ignore_index= True)
        # print(df.shape)
        # print(df.head(2))
        return df

    def read_all_sql_table(self):
        table_names = np.array(['House', 'HouseLocation', 'Price', 'Lister'])
        for table in table_names:
            self.read_sql_table(table)

    def join_tables(self):
        """
        (Hard coding) Default using the real estate database
        """
        table_names = np.array(['House', 'HouseLocation', 'Price', 'Lister'])
        self._df = self.read_sql_table(table_names[0])
        for table in table_names[1:]:
            df_table = self.read_sql_table(table).drop(labels= ['id'], axis= 1)
            self._df = pd.merge(self._df, df_table, how= 'left', 
                                left_on= 'id', right_on= 'house_id')
            if 'house_id' in self._df.columns:
                self._df = self._df.drop(labels= ['house_id'], axis= 1)
        # print(self._df.head(2))

    def convert_geo(self):
        self._df['lat_long'] = list(zip(self._df['latitude'], self._df['longitude']))
        rg_result = rg.search(self._df['lat_long'].tolist())
        df_geo = json_normalize(rg_result)
        self._df['area'] = df_geo['name']
        self._df['location'] = df_geo['admin2']
        # return json_normalize(rg_result)

    def dummy_feature(self, df, feature):
        dummies_feature = pd.get_dummies(df[feature]).columns
        self._feature = np.append(self._feature, dummies_feature)
        return pd.concat([df, pd.get_dummies(df[feature])], axis= 1)

    def feautre_label_encoder(self, df, feature):
        le = preprocessing.LabelEncoder()
        return df[[feature]].apply(le.fit_transform)[feature]

    def preprocessing_data(self):
        if not self._df.empty:
            print('Preprocessing data...')
            self._df.drop(labels= ['price_id'], axis= 1)
            self._df['bedroom_num'] = pd.to_numeric(self._df['bedroom_num'])
            self._df['bathroom_num'] = pd.to_numeric(self._df['bathroom_num'])
            self._df['car_spaces'] = pd.to_numeric(self._df['car_spaces'])
            self._df['dt'] = pd.to_datetime(self._df['post_time'], unit= 's')
            self._df['latitude_longitude'] = self._df[['latitude', 'longitude']].to_dict('records')
            # print(self._df[['latitude_longitude', 'area']].head(2))

    def load_train1_data(self):
        print('Loading train1 data...')
        self._feature = np.array(['bedroom_num'])
        self._df_train = self._df[(self._df['type'] == 'house') | (self._df['type'] == 'flat')]
        self._df_train = self._df_train.dropna(subset= ['bedroom_num'])
        self._target = self._df_train['price']

    def load_train2_data(self):
        print('loading train2 data...')
        self._feature = np.array(['bedroom_num'])
        self.convert_geo()
        self._df_train = self._df[(self._df['type'] == 'house') | (self._df['type'] == 'flat')]
        self._df_train = self._df_train.dropna(subset= ['bedroom_num'])
        self._df_train.index = range(len(self._df_train))
        self._df_train = self.dummy_feature(self._df_train, 'location')

    def split_train_test_data(self, cols):
        self._X_train, self._X_test, self._Y_train, self._Y_test  = train_test_split(self._df_train[cols], 
                                                                          self._target, test_size= 0.3, random_state= 50)

    def do_predict_LinearR(self):
        print('Building Linear Regression Model:')
        # self._features = np.array(['bedroom_num'])
        self.split_train_test_data(cols= self._features)
        self._clf = LinearRegression(normalize= True).fit(self._X_train, self._Y_train)
        print(f'fit score : {self._clf.score(self._X_test, self._Y_test)}')
        
    def evaluate_model(self):
        print('Model evaluation: ')
        print(cross_val_score(self._clf, self._X_test, self._Y_test, cv= 3))

    def export2db_clf(self):
        """
        Insert trained clf into database
        """
        try:
            if self._clf:
                query = """ INSERT INTO Model (title, algorithm, features, data_size, clf, version)
                            VALUES (%(title)s, %(algorithm)s, %(features)s, 
                                    %(data_size)s, %(clf)s, %(version)s)"""
                query_values = {"title": "baseline", "algorithm" : "LinearRegression", "features" : self._features.tolist(),
                                "data_size" : self._X_train.shape, 
                                "clf" : pickle.dumps(self._clf), "version" : '1.0'}
                self._db.cursor.execute(query, query_values)
                self._db.connection.commit()
            else:
                print('No avaliable trained classifier!')
        except Exception as e:
            print(e)

    def load_db_clf(self):
        try:
            query = """ SELECT clf FROM Model WHERE id = 1 """
            self._db.cursor.execute(query)
            clf= self._db.cursor.fetchone()[0]
            print(clf)
            return pickle.loads(clf)
        except Exception as e:
            print(e)

    def export2csv(self):
        print(self._df.shape)
        print(self._df.empty)
        if not self._df.empty:
            print('exporting data')
            self._df.to_csv('test.csv', index= False)
            
    def check(self):
        print(self._df.info())

    @property
    def data(self):
        return self._df


if __name__ == '__main__':
    user = 'postgres'
    password = 'root'
    db_name = 'real_estate'
    db_psql = DBPsql()
    ml = ML(db_psql)
    ml.connect2db()
    ml.join_tables()
    ml.preprocessing_data()
    # ml.check()
    ml.load_train2_data()
    ml.do_predict_LinearR()
    ml.evaluate_model()
    # ml.export2db_clf()
    # test_clf = ml.load_db_clf()
    # print(type(test_clf))
    # ml.export2csv()
    # ml.close_db_connection()
    # test_clf = ml.load_db_clf()