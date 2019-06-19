import os
import sys
sys.path.append('..')
sys.path.append(os.path.join('..', 'db'))

import numpy as np 
import pandas as pd  
import matplotlib.pyplot as pyplot

from sklearn import preprocessing
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix

from db_psql import DBPsql

class ML:
    def __init__(self, db):
        self._db = db
        self._df = pd.DataFrame()
        self._df_train = None
        self._target = None
        self._X_train = None
        self._X_test = None
        self._Y_train = None
        self._Y_test = None
        self._clf = None

    def connect2db(self):
        self._db.connect()
    
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

    def preprocessing_data(self):
        if not self._df.empty:
            self._df.drop(labels= ['price_id'], axis= 1)
            self._df['bedroom_num'] = pd.to_numeric(self._df['bedroom_num'])
            self._df['bathroom_num'] = pd.to_numeric(self._df['bathroom_num'])
            self._df['car_spaces'] = pd.to_numeric(self._df['car_spaces'])
            self._df['dt'] = pd.to_datetime(self._df['post_time'], unit= 's')
            self._df['lat_long'] = self._df[['latitude', 'longitude']].to_dict('records')

    def load_train_data(self):
        print('Loading train data...')
        self._df_train = self._df[(self._df['type'] == 'house') | (self._df['type'] == 'flat')]
        self._df_train = self._df_train.dropna(subset= ['bedroom_num'])
        self._target = self._df_train['price']

    def split_train_test_data(self, cols):
        self._X_train, self._X_test, self._Y_train, self._Y_test  = train_test_split(self._df_train[cols], 
                                                                          self._target, test_size= 0.3, random_state= 50)

    def do_predict_LinearR(self):
        print('Building Linear Regression Model:')
        self.split_train_test_data(cols= ['bedroom_num'])
        self._clf = LinearRegression(normalize= True).fit(self._X_train, self._Y_train)
        print(f'fit score : {self._clf.score(self._X_test, self._Y_test)}') 

    def evaluate_model(self):
        print('Model evaluation: ')
        print(cross_val_score(self._clf, self._X_test, self._Y_test, cv= 3))

    def export2db(self):
        pass
    
    def export2csv(self):
        print(self._df.shape)
        print(self._df.empty)
        if not self._df.empty:
            print('exporting data')
            self._df.to_csv('test.csv', index= False)
            
    def check(self):
        # print(self._df.info())
        # self._df['bedroom_num'] = pd.to_numeric(self._df['bedroom_num'])
        print(self._df.info())

user = 'postgres'
password = 'root'
db_name = 'real_estate'
db_psql = DBPsql(user, password, db_name)
# db_psql.connect()

ml = ML(db_psql)
ml.connect2db()
ml.join_tables()
ml.preprocessing_data()
# ml.check()
ml.load_train_data()
ml.do_predict_LinearR()
ml.evaluate_model()
# ml.export2csv()