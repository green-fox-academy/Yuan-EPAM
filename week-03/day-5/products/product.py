from flask import Flask, render_template, url_for

app = Flask(__name__)

products = [
    ("Milk", 3.59123),
    ("Bread", 2.96332),
    ("Rice", 0.64111)
]

@app.route('/products')
def list_product():
    return render_template('product.html', products= products)