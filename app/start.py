from flask import Flask, jsonify, request

from app.dao.product_brand_dao import ProductBrandDao
from app.dao.product_dao import ProductDao
from app.dao.product_rating_dao import ProductRatingDao
from app.dao.shipping_country_dao import ShippingCountryDao
from app.dao.product_category_dao import ProductCategoryDao
from app.dao.product_condition_dao import ProductConditionDao
from app.model.product import Product
from app.model.product_brand import ProductBrand
from app.model.product_condition import ProductCondition
from app.model.product_rating import ProductRating
from app.model.shipping_country import ShippingCountry
from app.model.product_category import ProductCategory


app = Flask(__name__)

p_dao = ProductDao()
p = Product()
p_brand_dao = ProductBrandDao()
p_brand = ProductBrand()

pr = ProductRatingDao()
sc = ShippingCountryDao()
p_category_dao = ProductCategoryDao()
p_condition_dao = ProductConditionDao()


@app.route('/')
def initial():
    return ' '


@app.route('/product', methods=['GET'])
def product():
    return jsonify([p.__dict__() for p in p_dao.read()]), 200


@app.route('/product', methods=['POST'])
def product_create():
    data = request.get_json()
    product = Product(**data)
    model = p_dao.create(product)
    return (jsonify(model.__dict__())), 201


@app.route('/product', methods=['DELETE'])
def product_delete():
    id = request.args.get('id')
    message = p_dao.delete(id)
    return jsonify(message), 200


# ------------------------------------------ Product Brand
@app.route('/product-brand', methods=['GET'])
def product_brand():
    return jsonify([p_brand.__dict__() for p_brand in p_brand_dao.read()]), 200


@app.route('/product-brand', methods=['POST'])
def product_brand_create():
    data = request.get_json()
    product_brand = ProductBrand(**data)
    model = p_brand_dao.create(product_brand)
    return (jsonify(model.__dict__())), 201


@app.route('/product-brand', methods=['DELETE'])
def product_brand_delete():
    id = request.args.get('id')
    message = p_brand_dao.delete(id)
    return jsonify(message), 200
# ------------------------------------------ Product Brand finish


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


@app.route('/product-category', methods=['GET'])
def product_category():
    return jsonify([p_category.__dict__() for p_category in p_category_dao.read()]), 200


@app.route('/product-category', methods=['POST'])
def product_category_create():
    data = request.get_json()
    product_category = ProductCategory(**data)
    model = p_category_dao.create(product_category)
    return jsonify(model.__dict__()), 201


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
