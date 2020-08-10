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
    return jsonify([prod.__dict__() for prod in pd.read()]), 200

@app.route('/product-brand')
def product_brand():
    return jsonify([prod_br.__dict__() for prod_br in pbd.read()]), 200

@app.route('/product_rating')
def product_rating():
    return jsonify([prod_rat.__dict__() for prod_rat in pr.read()]), 200

@app.route('/shipping_country')
def shipping_country():
    return jsonify([ship_coun.__dict__() for ship_coun in sc.read()]), 200

@app.route('/product-category')
def product_category():
    return jsonify([p_category.__dict__() for p_category in p_category_dao.read()]), 200

@app.route('/product-condition')
def product_condition():
    return jsonify([p_condition.__dict__() for p_condition in p_condition_dao.read()]), 200

app.run(debug=True)
