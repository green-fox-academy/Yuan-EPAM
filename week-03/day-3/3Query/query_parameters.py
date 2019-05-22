import os
import csv, json
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

def read_csv_data(file_path):
    try:
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter= ';')
            res = []
            head = []
            for i, row in enumerate(csv_reader):
                if i == 0:
                    head = row
                    json_keys = dict.fromkeys(head)
                    continue
                res.append({head[x] : row[x] for x in range(len(row))})
            print(res)
            return res
    except IOError:
        print(f'Unable to read file {file_path}')

data_file_path = os.path.join(os.getcwd(), 'products.txt')
data_base = read_csv_data(data_file_path)
print(f'database file path: {data_file_path}')
print('Data base:')
print(data_base)

@app.route('/')
def search_form():
    return render_template('product.html')

@app.route('/result', methods= ['POST', 'GET'])
def get_result():
    if request.method == 'POST':
        search_target = request.form
        search_res = search_product(data_base, search_target)
        return render_template('search_result.html', search_res = search_res, target= search_target)

def search_product(data_base, target):
    res = []
    key = list(target.keys())[0]
    val = list(target.values())[0]
    for data in data_base:
        print(f'data: {data}')
        print(f'target: {key}')
        print(f'data[target]: {data[key]}')
        if data[key] == val: 
            res.append(data[key])
    return {key : res[0]}

# read_csv_data(os.getcwd() + '\\3Query\\products.txt')


