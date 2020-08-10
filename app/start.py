from flask import Flask

from app.dao.product_dao import ProductDao
from app.dao.product_rating_dao import ProductRatingDao


app = Flask(__name__)
pd = ProductDao()
pr = ProductRatingDao()

@app.route('/')
def initial():
    return pd.read()[0].__dict__()

@app.route('/product_rating')
def product_rating():
    return pr.read()[0].__dict__()

app.run(debug=True)

