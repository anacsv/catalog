from flask import Flask, jsonify, request

from app.dao.product_brand_dao import ProductBrandDao
from app.dao.product_dao import ProductDao
from app.dao.product_rating_dao import ProductRatingDao
from app.dao.shipping_country_dao import ShippingCountryDao
from app.dao.product_category_dao import ProductCategoryDao
from app.dao.product_condition_dao import ProductConditionDao
from app.model.product_condition import ProductCondition
from app.model.product_rating import ProductRating
from app.model.shipping_country import ShippingCountry

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

@app.route('/product/', methods=['GET'])
def product():
    return jsonify([prod.__dict__() for prod in pd.read()]), 200

@app.route('/product-brand')
def product_brand():
    return jsonify([prod_br.__dict__() for prod_br in pbd.read()]), 200

@app.route('/product-rating', methods=["GET"])
def product_rating():
    return jsonify([prod_rat.__dict__() for prod_rat in pr.read()]), 200

@app.route('/product-rating', methods=["POST"])
def product_rating_create():
    data = request.get_json()
    product_rating = ProductRating(**data)
    model = pr.create(product_rating)
    return (jsonify(model.__dict__()), 201)

@app.route('/shipping-country', methods=["GET"])
def shipping_country():
    return jsonify([ship_coun.__dict__() for ship_coun in sc.read()]), 200

@app.route('/shipping-country', methods=["POST"])
def shipping_country_create():
    data = request.get_json()
    shipping_country = ShippingCountry(**data)
    model = sc.create(shipping_country)
    return (jsonify(model.__dict__()), 201)

@app.route('/product-category')
def product_category():
    return jsonify([p_category.__dict__() for p_category in p_category_dao.read()]), 200

@app.route('/product-condition', methods=['GET'])
def product_condition():
    return jsonify([p_condition.__dict__() for p_condition in p_condition_dao.read()]), 200

@app.route('/product-condition', methods=['POST'])
def product_condition_create():
    data = request.get_json()
    product_condition = ProductCondition(**data)
    model = p_condition_dao.create(product_condition)
    return (jsonify(model.__dict__()), 201)

app.run(debug=True)
