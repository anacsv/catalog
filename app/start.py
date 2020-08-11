from flask import Flask, jsonify, request
from flask_restful import Api


from app.controller.product_brand_controller import ProductBrandController
from app.controller.product_rating_controller import ProductRatingController
from app.controller.shipping_country_controller import ShippingCountryController

from app.dao.product_dao import ProductDao
from app.dao.product_category_dao import ProductCategoryDao
from app.dao.product_condition_dao import ProductConditionDao
from app.model.product import Product
from app.model.product_condition import ProductCondition
from app.model.product_category import ProductCategory

#command+d -> ctrl+g

app = Flask(__name__)
api = Api(app)


p_dao = ProductDao()
p = Product()

p_category_dao = ProductCategoryDao()
p_condition_dao = ProductConditionDao()



# ------------------------------------------ Product Brand
api.add_resource(ProductBrandController, '/api/product-brand/', endpoint='product-brands')
api.add_resource(ProductBrandController, '/api/product-brand/<int:id>', endpoint='product-brand')
# ------------------------------------------ Product Brand finish


# ------------------------------------------ Product Rating init
api.add_resource(ProductRatingController, '/api/product-rating/', endpoint='product-ratings')
api.add_resource(ProductRatingController, '/api/product-rating/<int:id>', endpoint='product-rating')
# ------------------------------------------ Product Rating finish


# ------------------------------------------ Shipping Country init
api.add_resource(ShippingCountryController, '/api/shipping-country/', endpoint='shipping-countries')
api.add_resource(ShippingCountryController, '/api/shipping-country/<int:id>', endpoint='shipping-country')
# ------------------------------------------ Shipping Country finish

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

@app.route('/product', methods=['PUT'])
def product_update():
    data = request.get_json()
    product = Product(**data)
    message = p_dao.update(product)
    return jsonify(message), 200


@app.route('/product-category', methods=['GET'])
def product_category():
    return jsonify([p_category.__dict__() for p_category in p_category_dao.read()]), 200


@app.route('/product-category', methods=['POST'])
def product_category_create():
    data = request.get_json()
    product_category = ProductCategory(**data)
    model = p_category_dao.create(product_category)
    return jsonify(model.__dict__()), 201


@app.route('/product-category', methods=['PUT'])
def product_category_update():
    data = request.get_json()
    product_category = ProductCategory(**data)
    message = p_category_dao.update(product_category)
    return jsonify(message), 200


@app.route('/product-category', methods=['DELETE'])
def product_category_delete():
    id = request.args.get('id')
    message = p_category_dao.delete(id)
    return jsonify(message), 200


@app.route('/product-condition', methods=['GET'])
def product_condition():
    return jsonify([p_condition.__dict__() for p_condition in p_condition_dao.read()]), 200


@app.route('/product-condition', methods=['POST'])
def product_condition_create():
    data = request.get_json()
    product_condition = ProductCondition(**data)
    model = p_condition_dao.create(product_condition)
    return jsonify(model.__dict__()), 201


@app.route('/product-condition', methods=['PUT'])
def product_condition_update():
    data = request.get_json()
    product_condition = ProductCondition(**data)
    message = p_condition_dao.update(product_condition)
    return jsonify(message), 200


@app.route('/product-condition', methods=['DELETE'])
def product_condition_delete():
    id = request.args.get('id')
    message = p_condition_dao.delete(id)
    return jsonify(message), 200






app.run(debug=True)
