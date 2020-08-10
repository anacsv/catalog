from flask import Flask

from app.dao.product_dao import ProductDao
from app.dao.product_rating_dao import ProductRatingDao
from app.dao.shipping_country_dao import ShippingCountryDao


app = Flask(__name__)
pd = ProductDao()
pr = ProductRatingDao()
sc = ShippingCountryDao()

@app.route('/')
def initial():
    return pd.read()[0].__dict__()

@app.route('/product_rating')
def product_rating():
    return pr.read()[0].__dict__()

@app.route('/shipping_country')
def shipping_country():
    return sc.read()[0].__dict__()

app.run(debug=True)

