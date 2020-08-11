from flask import Flask, jsonify, request
from flask_restful import Api


from app.controller.product_brand_controller import ProductBrandController
from app.controller.product_category_controller import ProductCategoryController
from app.controller.product_condition_controller import ProductConditionController


from app.dao.product_dao import ProductDao
from app.dao.product_rating_dao import ProductRatingDao
from app.dao.shipping_country_dao import ShippingCountryDao
from app.model.product import Product
from app.model.product_rating import ProductRating
from app.model.shipping_country import ShippingCountry

#command+d -> ctrl+g

app = Flask(__name__)
api = Api(app)


p_dao = ProductDao()
p = Product()

pr = ProductRatingDao()
sc = ShippingCountryDao()


# ------------------------------------------ Product Brand
api.add_resource(ProductBrandController, '/api/product-brand/', endpoint='product-brands')
api.add_resource(ProductBrandController, '/api/product-brand/<int:id>', endpoint='product-brand')
# ------------------------------------------ Product Brand finish


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


# ------------------------------------------ Product Rating init
@app.route('/product-rating', methods=["GET"])
def product_rating():
    return jsonify([prod_rat.__dict__() for prod_rat in pr.read()]), 200

@app.route('/product-rating', methods=["POST"])
def product_rating_create():
    data = request.get_json()
    product_rating = ProductRating(**data)
    model = pr.create(product_rating)
    return (jsonify(model.__dict__()), 201)


@app.route('/product-rating', methods=['PUT'])
def product_rating_update():
    data = request.get_json()
    product_rating = ProductRating(**data)
    message = pr.update(product_rating)
    return jsonify(message), 200

@app.route('/product-rating', methods=['DELETE'])
def product_rating_delete():
    id = request.args.get('id')
    message = pr.delete(id)
    return jsonify(message), 200
# ------------------------------------------ Product Rating finish
# ------------------------------------------ Shipping Country init
@app.route('/shipping-country', methods=["GET"])
def shipping_country():
    return jsonify([ship_coun.__dict__() for ship_coun in sc.read()]), 200

@app.route('/shipping-country', methods=["POST"])
def shipping_country_create():
    data = request.get_json()
    shipping_country = ShippingCountry(**data)
    model = sc.create(shipping_country)
    return (jsonify(model.__dict__()), 201)

@app.route('/shipping-country', methods=['PUT'])
def shipping_country_update():
    data = request.get_json()
    shipping_country = ShippingCountry(**data)
    message = sc.update(shipping_country)
    return jsonify(message), 200

@app.route('/shipping-country', methods=['DELETE'])
def shipping_country_delete():
    id = request.args.get('id')
    message = sc.delete(id)
    return jsonify(message), 200
# ------------------------------------------ Shipping Country finish

api.add_resource(ProductCategoryController, '/api/product-category/', endpoint='product-categories')
api.add_resource(ProductCategoryController, '/api/product-category/<int:id>/', endpoint='product-category')


api.add_resource(ProductConditionController, '/api/product-condition/', endpoint='product-conditions')
api.add_resource(ProductConditionController, '/api/product-condition/<int:id>/', endpoint='product-condition')


app.run(debug=True)
