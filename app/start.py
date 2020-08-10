from flask import Flask, jsonify

from app.dao.product_brand_dao import ProductBrandDao
from app.dao.product_dao import ProductDao
from app.dao.product_rating_dao import ProductRatingDao
from app.dao.shipping_country_dao import ShippingCountryDao
from app.dao.product_category_dao import ProductCategoryDao
from app.dao.product_condition_dao import ProductConditionDao

app = Flask(__name__)

pd = ProductDao()
pbd = ProductBrandDao()
pr = ProductRatingDao()
sc = ShippingCountryDao()
p_category_dao = ProductCategoryDao()
p_condition_dao = ProductConditionDao()


@app.route('/')
def initial():
    return ' '

@app.route('/product')
def product():
    return pd.read()[0].__dict__()

@app.route('/product-brand')
def product_brand():
    return pbd.read()[0].__dict__()

@app.route('/product_rating')
def product_rating():
    return pr.read()[0].__dict__()

@app.route('/shipping_country')
def shipping_country():
    return sc.read()[0].__dict__()

@app.route('/product-category')
def product_category():
    return (jsonify( [pc.__dict__() for pc in p_category_dao.read() ]), 200)

@app.route('/product-condition')
def product_condition():
    return p_condition_dao.read()[0].__dict__()

app.run(debug=True)
